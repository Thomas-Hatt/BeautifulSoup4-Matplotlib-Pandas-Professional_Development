# Web Scraping with Python - Beautiful Soup Crash Course

This project demonstrates the use of Python and the Beautiful Soup library for web scraping. It is based on the **Beautiful Soup Crash Course** tutorial by freeCodeCamp.org. You'll learn how to parse an HTML file, extract specific elements, and display the desired data in a structured way.

---

# Requirements

To use this project, you'll need:
- Python installed on your machine (version 3.6 or above recommended, I used 3.13.2).
- The Beautiful Soup library for HTML parsing (`bs4`).
- The `lxml` parser library.

You can install the required libraries using pip:

```bash
pip install beautifulsoup4
pip install lxml
```
---

## Overview

The project features a Python script that:
1. Reads an HTML file (`home.html`).
2. Extracts and displays specific HTML elements, including:
   - All `<h5>` tags.
   - Course titles and prices.
3. Prints results in an organized format.