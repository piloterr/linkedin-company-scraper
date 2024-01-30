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

```json
{
  "https://linkedin.com/company/apple": {
    "founded": 1976,
    "tagline": null,
    "website": "http://www.apple.com/careers",
    "industry": "Computers and Electronics Manufacturing",
    "logo_url": "https://media.licdn.com/dms/image/C560BAQHdAaarsO-eyA/company-logo_200_200/0/1630637844948/apple_logo?e=2147483647&v=beta&t=xvKAJA_O8lN87HdM0DrITjC9jxtfvton5J7PhBI3cmw",
    "locations": [
      "1 Apple Park Way Cupertino, California 95014, US"
    ],
    "company_id": 162479,
    "company_url": "https://www.linkedin.com/company/apple",
    "description": "We’re a diverse collective of thinkers and doers, continually reimagining what’s possible to help us all do what we love in new ways. And the same innovation that goes into our products also applies to our practices — strengthening our commitment to leave the world better than we found it. This is where your work can make a difference in people’s lives. Including your own.\n\nApple is an equal opportunity employer that is committed to inclusion and diversity. Visit apple.com/careers to learn more.",
    "headquarter": {
      "city": "Cupertino",
      "line1": "1 Apple Park Way",
      "country": "US",
      "postal_code": "95014"
    },
    "staff_count": 167531,
    "staff_range": "over-10k",
    "company_name": "Apple",
    "specialities": [
      "Innovative Product Development",
      "World-Class Operations",
      "Retail",
      "Telephone Support"
    ],
    "similar_companies": [
      {
        "company_url": "https://www.linkedin.com/company/google",
        "company_logo": "https://media.licdn.com/dms/image/C4D0BAQHiNSL4Or29cg/company-logo_100_100/0/1631311446380?e=2147483647&v=beta&t=5bmvSDVt4i-ECxTU43yiS4iXUM4inJiG-e9PHOUlxx0",
        "company_name": "Google"
      },
      {
        "company_url": "https://www.linkedin.com/company/amazon",
        "company_logo": "https://media.licdn.com/dms/image/C560BAQHTvZwCx4p2Qg/company-logo_100_100/0/1630640869849/amazon_logo?e=2147483647&v=beta&t=ckUoyDcKb4OtrPrnkiepZRIH4rOREd9cewh-TTrMVJE",
        "company_name": "Amazon"
      },
      {
        "company_url": "https://www.linkedin.com/company/microsoft",
        "company_logo": "https://media.licdn.com/dms/image/C560BAQE88xCsONDULQ/company-logo_100_100/0/1630652622688/microsoft_logo?e=2147483647&v=beta&t=4ft1hh_UdO2TMuqRWlFPHTTr2B3BN0E2LmTE6tEYwJI",
        "company_name": "Microsoft"
      },
      {
        "company_url": "https://www.linkedin.com/company/netflix",
        "company_logo": "https://media.licdn.com/dms/image/C4E0BAQEVb0ZISWk8vQ/company-logo_100_100/0/1631355051964?e=2147483647&v=beta&t=_82G5gJfq-rmofKHPHZOMBYvtHfTF8Z2qA_zAUvcVV4",
        "company_name": "Netflix"
      },
      {
        "company_url": "https://www.linkedin.com/company/meta",
        "company_logo": "https://media.licdn.com/dms/image/C4E0BAQFdNatYGiBelg/company-logo_100_100/0/1636138754252/facebook_logo?e=2147483647&v=beta&t=ULaTUKRgzMzLCy5-pLoRMfMKpEI4OApXM5C9pEDZSDs",
        "company_name": "Meta"
      },
      {
        "company_url": "https://www.linkedin.com/company/tesla-motors",
        "company_logo": "https://media.licdn.com/dms/image/C4D0BAQHUcu98SZ2TVw/company-logo_100_100/0/1630576446368/tesla_motors_logo?e=2147483647&v=beta&t=fFZSy_dnN_IDaC_6hHxOobiRkj_4lybAf3Nf5AalKTk",
        "company_name": "Tesla"
      },
      {
        "company_url": "https://se.linkedin.com/company/spotify",
        "company_logo": "https://media.licdn.com/dms/image/C560BAQFkDzx_7dqq3A/company-logo_100_100/0/1631377935713?e=2147483647&v=beta&t=NwnhQQRVNLNgsEv90Wv1IYzpZ5RxKEICx6TaqeFxX7M",
        "company_name": "Spotify"
      },
      {
        "company_url": "https://www.linkedin.com/company/ibm",
        "company_logo": "https://media.licdn.com/dms/image/D560BAQGiz5ecgpCtkA/company-logo_100_100/0/1688684715866/ibm_logo?e=2147483647&v=beta&t=5zkuzxYrW1Iyx8oUa-u7lMSQ9TN1Q9D87M_0ybQf3NQ",
        "company_name": "IBM"
      },
      {
        "company_url": "https://www.linkedin.com/company/linkedin",
        "company_logo": "https://media.licdn.com/dms/image/C560BAQHaVYd13rRz3A/company-logo_100_100/0/1638831590218/linkedin_logo?e=2147483647&v=beta&t=wQTMb6WSKjpi2vWVLKyWcrO7wtW-3uoVDhQ7ka58vhA",
        "company_name": "LinkedIn"
      },
      {
        "company_url": "https://www.linkedin.com/company/deloitte",
        "company_logo": "https://media.licdn.com/dms/image/C560BAQGNtpblgQpJoQ/company-logo_100_100/0/1662120928214/deloitte_logo?e=2147483647&v=beta&t=KhIfaHWyu1aAgyyImEhYDprMjFP3LaMR0E7NF2MPxMY",
        "company_name": "Deloitte"
      }
    ],
    "affiliated_companies": []
  },
  "https://linkedin.com/company/boeing": {
    "founded": 1916,
    "tagline": "Join us and find an inclusive workplace built on innovation and shared values. ",
    "website": "http://www.boeing.com",
    "industry": "Aviation and Aerospace Component Manufacturing",
    "logo_url": "https://media.licdn.com/dms/image/C4E0BAQHpXZDZYImrdA/company-logo_200_200/0/1630572987498/boeing_logo?e=2147483647&v=beta&t=D_PAe-IUw4uIUbcQrB8f030hTr6varX7J0Fpcrsp5CY",
    "locations": [
      "929 Long Bridge Drive Arlington, VA 22202, US",
      "100 N. Riverside Chicago, IL 60606-1596, US",
      "499 Boeing Blvd SW Huntsville, AL 35824, US",
      "460 Herndon Pkwy Herndon, VA 20170, US",
      "3455 Airframe Dr North Charleston, SC 29418, US",
      "45 O'Connor St Ottawa, ON K1P 1A4, CA",
      "320 Wooten Rd Colorado Springs, CO 80916, US",
      "15059 Conference Center Dr Chantilly, VA 20151, US",
      "Avenida Sur del Aeropuerto de Barajas, 38 Madrid, Community of Madrid 28042, ES",
      "30 Changi North Rise Singapore, Singapore 498780, SG",
      "3265 160th Ave SE Bellevue, WA 98008, US",
      "6200 James S McDonnell Blvd Berkeley, MO 63134, US",
      "N 6th St Renton, WA 98057, US",
      "5905 Legacy Drive Ste. 325 Plano, Texas 75024, US"
    ],
    "company_id": 1384,
    "company_url": "https://www.linkedin.com/company/boeing",
    "description": "We are the world’s largest aerospace company and leading provider of commercial airplanes, defense, space and security systems, and global services. Building on a legacy of aerospace leadership, Boeing continues to lead in technology and innovation, deliver for its customers, and invest in its people and future growth.\nWith us you can create and contribute to what matters most in your career, in your community and around the world. Our team members are supported to explore their professional interests and pursue new opportunities that will deepen their knowledge of our business. Join us in building the future of aerospace: boeing.com/careers\nBoeing is an Equal Opportunity Employer. Employment decisions are made without regard to race, color, religion, national origin, gender, sexual orientation, gender identity, age, physical or mental disability, genetic factors, military/veteran status or other characteristics protected by law.",
    "headquarter": {
      "city": "Arlington",
      "line1": "929 Long Bridge Drive",
      "country": "US",
      "postal_code": "22202"
    },
    "staff_count": 112930,
    "staff_range": "over-10k",
    "company_name": "Boeing",
    "specialities": null,
    "similar_companies": [
      {
        "company_url": "https://fr.linkedin.com/company/airbusgroup",
        "company_logo": "https://media.licdn.com/dms/image/C4D0BAQF2j_LDG_TOzg/company-logo_100_100/0/1631375371456/airbusgroup_logo?e=2147483647&v=beta&t=Qv6aA59zR45wcTFug7eOkahETMqR24vccuIXwbyS8qk",
        "company_name": "Airbus"
      },
      {
        "company_url": "https://www.linkedin.com/company/lockheed-martin",
        "company_logo": "https://media.licdn.com/dms/image/C4E0BAQHF1YKEZdN4LA/company-logo_100_100/0/1668532986109/lockheed_martin_logo?e=2147483647&v=beta&t=MAt3FDVkp1mxAnqi-7a-mmVAi8Lcd_S1_XvT0Y_Z40s",
        "company_name": "Lockheed Martin"
      },
      {
        "company_url": "https://www.linkedin.com/company/northrop-grumman-corporation",
        "company_logo": "https://media.licdn.com/dms/image/C4E0BAQFnJf3Nn259IA/company-logo_100_100/0/1630610111160/northrop_grumman_corporation_logo?e=2147483647&v=beta&t=PhJhVuWyHHu1DrGQDXndP1CPgPrnf_BKye-Lw_JA4s8",
        "company_name": "Northrop Grumman"
      },
      {
        "company_url": "https://www.linkedin.com/company/geaerospace",
        "company_logo": "https://media.licdn.com/dms/image/D560BAQGEU0_PAp08RQ/company-logo_100_100/0/1684425911325/geaerospace_logo?e=2147483647&v=beta&t=hUPcyP3Zi1NxNpMrT3eDn8JcmW89vums-nJj9-QW6nU",
        "company_name": "GE Aerospace"
      },
      {
        "company_url": "https://uk.linkedin.com/company/rolls-royce",
        "company_logo": "https://media.licdn.com/dms/image/D4E0BAQG026Y0w2F9ZA/company-logo_100_100/0/1688142449677/rolls_royce_logo?e=2147483647&v=beta&t=DxLuJyc1AIZaB4FwCY_fRAfjwtPwlmQtHBYXqluPCic",
        "company_name": "Rolls-Royce"
      },
      {
        "company_url": "https://www.linkedin.com/company/collins-aerospace",
        "company_logo": "https://media.licdn.com/dms/image/D560BAQGOO3rPemY70w/company-logo_100_100/0/1687169228108/collins_aerospace_logo?e=2147483647&v=beta&t=-BuXtIe-zBnRVeQ5kGX-GzzBpUUb1lR215HgKWP1g20",
        "company_name": "Collins Aerospace"
      },
      {
        "company_url": "https://www.linkedin.com/company/rtx",
        "company_logo": "https://media.licdn.com/dms/image/D560BAQFITBtnCzFO9w/company-logo_100_100/0/1687169432565/raytheontechnologies_logo?e=2147483647&v=beta&t=wSI5b0XsYZFvCdsSR52EXU5bNreSfIMhkumtdrzH1GI",
        "company_name": "RTX"
      },
      {
        "company_url": "https://www.linkedin.com/company/spacex",
        "company_logo": "https://media.licdn.com/dms/image/C560BAQEbqLQ-JE0vdQ/company-logo_100_100/0/1630604387686/spacex_logo?e=2147483647&v=beta&t=DP_P06ZVq-UNBKpivajePHCtUV1vTha7ehRNveffons",
        "company_name": "SpaceX"
      },
      {
        "company_url": "https://www.linkedin.com/company/nasa",
        "company_logo": "https://media.licdn.com/dms/image/C4D0BAQGRBHWCcaAqGg/company-logo_100_100/0/1630507197379/nasa_logo?e=2147483647&v=beta&t=QwvsU52A0lZ-cCZinp8M6LJjT1OKeVB_r8OI3cbPUj4",
        "company_name": "NASA - National Aeronautics and Space Administration"
      },
      {
        "company_url": "https://www.linkedin.com/company/google",
        "company_logo": "https://media.licdn.com/dms/image/C4D0BAQHiNSL4Or29cg/company-logo_100_100/0/1631311446380?e=2147483647&v=beta&t=5bmvSDVt4i-ECxTU43yiS4iXUM4inJiG-e9PHOUlxx0",
        "company_name": "Google"
      }
    ],
    "affiliated_companies": [
      {
        "company_url": "https://www.linkedin.com/company/cdg-a-boeing-company",
        "company_logo": "https://media.licdn.com/dms/image/C4E0BAQHDaM1y-dOlYQ/company-logo_100_100/0/1631346571987?e=2147483647&v=beta&t=q3IhciYRndoHpy_uWNGJ5yvRn6Pf1I7yQKa9bgIC-TM",
        "company_name": "CDG, a Boeing Company"
      },
      {
        "company_url": "https://ca.linkedin.com/company/boeingvancouver",
        "company_logo": "https://media.licdn.com/dms/image/C510BAQFejLhKzkTN2g/company-logo_100_100/0/1631432167290?e=2147483647&v=beta&t=f6tf4EiMeTpnjFZx7UJWemixMNsnubf7OlPiLSezYbQ",
        "company_name": "Boeing Vancouver"
      }
    ]
  }
}
```

Additionally, it maintains a record of failed rows in `failed_rows.txt` for reprocessing in subsequent runs.

## Contributing

Feel free to contribute by submitting issues or pull requests. Your feedback and improvements are welcome!