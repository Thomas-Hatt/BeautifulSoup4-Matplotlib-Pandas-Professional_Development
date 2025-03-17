# Program Visualization and Data Extraction Tool

This project includes tools for extracting program data from a web catalog and visualizing the extracted information. It processes academic programs, categorizes them, and provides interactive visualizations. 

I've used data collected from Mott Community College's "Programs of Study" website. I've organized them by using the matplotlib, pandas, and BeautifulSoup libraries.

`programs.csv` is pregenerated, so it is not necessary that you run `program_scraper.py` yourself unless you'd like to experiment with the methodologies I've used.

There is extensive documentation is both of my Python scripts, so you can read more into how things are made.

# Prerequisites

Ensure you have Python installed along with the following libraries:
- `pandas`
- `matplotlib`
- `BeautifulSoup` (from `bs4`) --- Please Note: this is only required if you wish to use `program_scraper.py`
- `requests`

You can install the required libraries with:
```bash
pip install pandas 
pip install matplotlib 
pip install beautifulsoup4 
pip install requests
```

## Features

- **Data Extraction**: Scrape program information and links from the MCC catalog and save it to a CSV file.
- **Program Categories Distribution**: Visualize the distribution of program types (e.g., Certificate, A.A.S., Associate).
- **Field Distribution**: Identify fields (e.g., Technology, Health, Arts) associated with various programs.
- **Top Keywords**: Display the most common keywords used in program names.

---

## How it Works
- The `program_scraper.py` script scrapes program information and their respective links from the MCC catalog website, then saves this data to a CSV file (programs.csv).
- The `visualize_programs.py` script scrapes from https://catalog.mcc.edu/content.php?catoid=17&navoid=518 and processes the `programs.csv` file to generate insights and visualizations based on program categories, fields, and common keywords.

### Programs are categorized into:

- Associate Degrees

- Certificates

- Alternative Training (A.K.A 'Other')

Each program's name and link are saved to a CSV file:
---

Column 1: URL

Column 2: Program

https://catalog.mcc.edu/preview_program.php?catoid=17&poid=2034&returnto=518, Associate in Science

https://catalog.mcc.edu/preview_program.php?catoid=17&poid=2035&returnto=518, Certificate in Cybersecurity
Processing the Data

The `visualize_programs.py` script categorizes programs, maps them to specific fields, and provides visual insights. I have provided screenshots within the `findings` folder located in the same directory.

---