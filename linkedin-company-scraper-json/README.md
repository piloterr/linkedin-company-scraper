# LinkedIn Company Information Retrieval Script

## Overview

This Python script is designed to retrieve information about LinkedIn companies using their slugs. It makes use of the Piloterr API to fetch data and stores the results in a JSON file. The script utilizes concurrent programming for efficient processing and includes error handling mechanisms to handle HTTP and request errors.

## Prerequisites

Before running the script, make sure to set up the following:

- Python environment
- Required Python packages: `dotenv`, `requests`, `tqdm`, `termcolor`
- API Token: Obtain an API token from Piloterr and set it in the `.env` file.

## Usage

1. Install the required packages:

```bash
pip install dotenv requests tqdm termcolor
```

2. Set up the API token:

- Create a `.env` file in the script directory.
- Add the following line with your Piloterr API token:

```plaintext
API_TOKEN=your_api_token_here
```

- Change the `MAX_WORKERS` variable in the script to set the number of concurrent workers.
- Save the file.

3. Prepare the CSV file:

- Create a CSV file named `extract.csv` with a column containing LinkedIn company slugs.

4. Run the script:

```bash
python linkedin_company.py
```

## Results

The script outputs the retrieved company information in a JSON file named `results.json`. 

Additionally, it maintains a record of failed rows in `failed_rows.txt` for reprocessing in subsequent runs.

## Contributing

Feel free to contribute by submitting issues or pull requests. Your feedback and improvements are welcome!