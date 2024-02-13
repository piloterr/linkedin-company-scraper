import os
import requests
import csv
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Semaphore, Lock
from dotenv import load_dotenv
from termcolor import colored
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("API_TOKEN")
MAX_WORKERS = int(os.getenv("MAX_WORKERS", 5))

# Semaphore to limit concurrent requests per second
semaphore = Semaphore(MAX_WORKERS)

# Thread lock to synchronize access to the JSON file
json_file_lock = Lock()

# Request to the API with rate limiting
def get_company_info(slug):
    with semaphore:
        url = f"https://piloterr.com/api/v2/linkedin/company/info?query={slug}"
        headers = {"x-api-key": TOKEN}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            company_info = response.json()
            # Update the JSON file with each successful response
            update_json(slug, company_info)
            return company_info
        except requests.exceptions.HTTPError as http_err:
            # See 404, 500, etc. errors
            # print(f"HTTP error occurred: {http_err}")
            pass
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        finally:
            # Wait before releasing the semaphore to adhere to rate limit
            time.sleep(1 / 5)  # Wait 1/5th of a second before allowing a new request

# Update the JSON file with the company information
def update_json(slug, company_info):
    with json_file_lock:  # Use a lock to prevent concurrent access to the file
        try:
            with open('results.json', 'r', encoding='utf-8') as json_file:
                result_dict = json.load(json_file)
        except FileNotFoundError:
            result_dict = {}
    
        result_dict[slug] = company_info
    
        with open('results.json', 'w', encoding='utf-8') as json_file:
            json.dump(result_dict, json_file, ensure_ascii=False, indent=2)

# Process slugs from a CSV file with progress bar
def process_slugs(rows):
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(get_company_info, row[0]): row[0] for row in rows}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Rows", unit="row"):
            slug = futures[future]
            try:
                data = future.result()
                # Process the received data if necessary
            except Exception as e:
                print(f"An error occurred for {slug}: {e}")

# Main script execution
if __name__ == "__main__":
    csv_file = 'extract.csv'
    failed_rows = []

    # Load failed rows if the file exists
    try:
        with open('failed_rows.txt', 'r', encoding='utf-8') as failed_file:
            failed_rows = [int(line.strip()) for line in failed_file]
    except FileNotFoundError:
        pass

    # Read the CSV file with company slugs
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Save the header
        rows = [row for row in csv_reader if row]  # Save the rows

    # Process the rows with rate limiting and progress indication
    process_slugs(rows)

    # Save the list of failed rows for the next run
    with open('failed_rows.txt', 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(map(str, failed_rows)))

    print(colored("Script execution completed successfully.", "green"))
