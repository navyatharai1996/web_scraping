# Web Scraping – Job Discovery Tool

A Python tool that collects job listings from a webpage, filters job titles by keyword and exports matching results to a CSV file.

Built as a practical project covering web scraping, HTML parsing, text filtering and structured data export.

## Features

- Download webpage HTML using Python’s built-in `urllib`.
- Extract job titles, companies and locations with Beautiful Soup.
- Filter titles using configurable keywords.
- Record the first matching keyword for each job.
- Display matching jobs and their total count.
- Export results to an Excel-compatible CSV file.

## Data Source

This project uses Python’s sample job listings, provided for web scraping practice.

The listings are fictional and demonstrate the tool’s functionality.

Source: https://realpython.github.io/fake-jobs/

## How It Works

1. Send an HTTP request to retrieve the webpage.
2. Parse the HTML with Beautiful Soup.
3. Locate each job card and extract its details.
4. Check each title against the keyword list.
5. Store matching jobs as Python dictionaries.
6. Write the results to `matching_jobs.csv`.

## Technology

- Python 3
- Beautiful Soup 4
- Python standard library modules: `urllib.request`, `csv` and `pathlib`

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/navyatharai1996/web_scraping.git
cd web_scraping
```

### 2. Create a virtual environment

On Windows:

```powershell
py -m venv .venv
```

### 3. Run the tool

```powershell
.\.venv\Scripts\python.exe job_discovery.py
```

The script prints matching jobs and saves `matching_jobs.csv` beside the Python file.

## Customise the Search

Edit the keyword list in `job_discovery.py`:

```python
keywords = ["python", "software", "data"]
```

Matching is case-insensitive and checks for substrings within job titles. For example, `data` matches both “Data scientist” and “Database administrator”.

Each matching job is stored once, along with the first keyword that matched.

## Output

The CSV contains these columns:

| Column | Description |
| --- | --- |
| title | Job title |
| company | Company name |
| location | Listed job location |
| matched_keyword | First keyword matched in the title |

Each run replaces the previous CSV output. Close the CSV in Excel before running the script again.

## Project Files

```text
job_discovery.py      Main scraping and export script
.gitignore            Files excluded from version control
README.md             Project overview and instructions
matching_jobs.csv     Generated output
Project Documentation.docx
```

## Current Scope

The tool processes one webpage and filters job titles. Its HTML selectors are specific to the sample website and need adapting for other sources.

## What I Practised

- Retrieving webpage content through HTTP requests
- Identifying HTML elements using tags and CSS classes
- Extracting and cleaning text
- Applying case-insensitive keyword filters
- Organising records with lists and dictionaries
- Exporting structured data to CSV
- Managing dependencies with a virtual environment
- Tracking project changes with Git and GitHub

## Author

Navyatha Rai  
https://github.com/navyatharai1996
