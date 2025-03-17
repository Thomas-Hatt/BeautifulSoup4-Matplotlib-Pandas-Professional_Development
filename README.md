# Web Scraping and Data Analysis with Python

## Technical Upskilling: BeautifulSoup, Pandas, and Matplotlib

### Web Scraping Fundamentals with BeautifulSoup
As part of my technical upskilling, I completed **freeCodeCamp.org**'s [*Web Scraping with Python - BeautifulSoup Crash Course (2020)*](https://www.youtube.com/watch?v=XVv6mJpFOb0). Key learnings include:

#### Phase 1: Static Webpage Parsing
- **Objective**: Parse a locally stored webpage using the `lxml` parser.
- **Process**:
  - Extracted raw HTML structure for preliminary analysis.
  - Isolated `<h5>` elements, yielding outputs like:
    ```python
    [<h5 class="card-title">Python for beginners</h5>, 
     <h5 class="card-title">Python Web Development</h5>, 
     <h5 class="card-title">Python Machine Learning</h5>]
    ```
  - Refined extraction by looping through tags to retrieve clean text:
    ```
    Python for beginners, Python Web Development, Python Machine Learning
    ```
  - Targeted `<div class="card">` containers to structure course titles and pricing data.

#### Phase 2: Dynamic Content Extraction (TimesJobs Case Study)
- **Scope**: Scraped real-time job listings under "Mobile Application Development."
- **Methodology**:
  1. **Observation**: Identified key attributes (job title, skills, date, employer).
  2. **Technical Inspection**: Analyzed hierarchical `<div>` structures (*Figure 1*).
  3. **Advanced Extraction**:
     - **Company Name**: `<h3 class="joblist-comp-name">`
     - **Job Title**: `<h2 class="heading-trun">` (via `title` attribute)
     - **Publication Date**: `<span class="sim-posted">`
     - **Key Skills**: `<div class="more-skills-sections">`
  - **Output**:
    ```
    Job Title: Android Developer
    Company: SEVEN CONSULTANCY
    Skills: java, mobile, mobile application development
    ```

---

## Independent Case Study: Academic Program Analysis
**Project**: Analysis of *Mott Community College’s Programs of Study 2024-2025*.

### Workflow
1. **Data Acquisition**:
   - Script: `program_scraper.py`
   - Output: Structured `programs.csv` with columns:
     ```csv
     https://catalog.mcc.edu/preview_program.php?catoid=17&poid=2034&returnto=518, Associate in Science
     ```
2. **Analytical Processing**:
   - Script: `visualize_programs.py`
   - Tools: `pandas` for categorization, `matplotlib` for visualization.
   - Categories:
     - *Associate Degrees* (e.g., *Associate in Science*)
     - *Certificates* (e.g., *Certificate in Cybersecurity*)
     - *Alternative Training* (labeled as *Other*)

### Technical Implementation
- **Visual Analytics**:
  - **Horizontal Bar Graphs**: Keyword frequency (e.g., "Technology," "Management").
  - **Pie Charts**: Program distribution across fields (Technology, Health, Arts).
  - Outputs saved to `/findings` directory (*Figure 5. Top 10 Most Common Keywords*).

---

## Conclusion
Completing this curriculum reinforced:
1. The transformative role of computational tools in deriving insights from unstructured data.
2. The importance of structured learning for technical proficiency in:
   - Dynamic content extraction
   - Data visualization (`matplotlib`, `pandas`)
3. Applications in academic and professional contexts, particularly for data science and analysis.