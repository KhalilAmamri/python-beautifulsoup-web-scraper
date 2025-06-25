# YallaKora Match Scraper

This Python script scrapes football match details from the YallaKora website for a specified date and saves the data into a CSV file.

## Features

- Accepts a date input in `dd-mm-yyyy` format.
- Validates the date format before proceeding.
- Converts the date to the format expected by the YallaKora website URL.
- Scrapes match details including championship, teams, score, and match time.
- Saves the scraped data into a CSV file named `matches_dd-mm-yyyy.csv`.
- Writes CSV files with UTF-8 BOM encoding and semicolon delimiters for Excel compatibility.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the script:

```bash
python yallakora_scraper.py
```

2. When prompted, enter the date in `dd-mm-yyyy` format (e.g., `25-06-2025`).

3. The script will fetch match details for the specified date and save them in a CSV file in the project directory.

## Notes

- The script converts the input date to the format `m/d/yyyy` as required by the YallaKora website.
- The CSV file uses semicolon (`;`) as the delimiter to ensure proper display in Excel for certain locales.
- The CSV file is saved with UTF-8 BOM encoding to avoid character encoding issues in Excel.

## Example

Input:

```
please enter the date in  format: dd-mm-yyyy: 25-06-2025
```

Output:

```
Matches details for 25-06-2025 have been written to matches_25-06-2025.csv
```

## License

This project is licensed under the MIT License.
