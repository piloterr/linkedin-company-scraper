import os
from dotenv import load_dotenv
import requests
import csv
import time
import json
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from termcolor import colored

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("API_TOKEN")
MAX_WORKERS = int(os.getenv("MAX_WORKERS", 1))

# Request to the API
def get_company_info(slug):
    url = f"https://piloterr.com/api/v2/linkedin/company/info?query={slug}"
    headers = {"x-api-key": TOKEN}

    try:
        with requests.get(url, headers=headers) as response:
            response.raise_for_status()
            company_info = response.json()
            # Update the JSON file with each successful response
            update_json(slug, company_info)
            return company_info
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None

# Function to update the JSON file
def update_json(slug, company_info):
    try:
        with open('results.json', 'r', encoding='utf-8') as json_file:
            result_dict = json.load(json_file)
    except FileNotFoundError:
        result_dict = {}

    result_dict[slug] = company_info

    with open('results.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict, json_file, ensure_ascii=False, indent=2)

# Read the CSV file with company slugs
csv_file = 'extract.csv'
failed_rows = []

try:
    with open('failed_rows.txt', 'r', encoding='utf-8') as failed_file:
        failed_rows = [int(line.strip()) for line in failed_file]
except FileNotFoundError:
    pass

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Save the header
    rows = list(csv_reader)   # Save the rows

# Progress bar for processing rows
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    for i, row in tqdm(enumerate(rows, start=1), total=len(rows), desc="Processing Rows", unit="row"):
        slug = row[0]

        # Check if the slug already exists in the JSON
        try:
            with open('results.json', 'r', encoding='utf-8') as json_file:
                result_dict = json.load(json_file)
        except FileNotFoundError:
            result_dict = {}

        if slug not in failed_rows:
            # Before making the API request, check if it has not already been sent
            if slug not in result_dict:
                company_info = executor.submit(get_company_info, slug).result()
                if company_info:
                    # No need to add to the dictionary here, as it is handled by the get_company_info function
                    pass
                else:
                    failed_rows.append(i)

# Save the list of failed rows for the next run
with open('failed_rows.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(map(str, failed_rows)))

print(colored("Script execution completed successfully.", "green"))
