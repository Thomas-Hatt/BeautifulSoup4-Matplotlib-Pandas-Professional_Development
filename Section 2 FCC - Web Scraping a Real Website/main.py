# pip install requests
from bs4 import BeautifulSoup
import requests

# -- -- PLEASE READ -- --
# Since this website is dynamically updated to show new jobs as they are uploaded, my code, comments, and analyses cannot accurately reflect how it is at a future date. The date that I am analyzing this on is March 15th, 2025.
# It is also possible that the structure of the HTML webpage could change in the future (which would render this code unusable), since it has changed since the original YouTube video upload date of November 18th, 2020
# You can read whichever section you find intriguing from now onwards, enjoy!


# For the analysis of the website https://www.timesjobs.com/ ,
# I searched for "Mobile Application Development"
# Since the webpage is dynamically updated, I chose not to specify any parameters.
# As of writing and developing this application on March 15th, 2025, there was 101 Jobs found.

# Here is the link to that version of the website: 
# https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=%22Mobile+Application+Development%22%2C&cboWorkExp1=2&txtLocation=



# -------------------------------------------------------------------------------------------------------------------------------------------

# -- Initial Analysis --
# # In the same directory, there is a screenshot (first_job_posting_main_page.png) that shows the following information for the job: 
# - Job posted by SEVEN CONSULTANCY
# - Industry: IT-Software
# - Specialization: Mobile
# - Qualification: Any Graduate
# - Job title is "Android Developer"
# - Job Location is "Navi Mumbai (Maharashtra), Mumbai (Maharashtra), Thane (Maharashtra)"
# - Job Function: IT Software : Software Products & Services
# - Employment Type: Full Time
# - Key Skills - java, mobile, mobile application development

# -------------------------------------------------------------------------------------------------------------------------------------------

# -- Initial Technical Analysis --
# All of the main content, including job postings, are under <div class="inside-rhs main-search-block">
# It is then separated by <div id="searchResultContents">
# The joblist is displayed in an unordered list <ul class="new-joblist">
# Each job posting is an object in the list categorized by <li class="clearfix job-bx wht-shd-bx">

# -------------------------------------------------------------------------------------------------------------------------------------------

# -- Further Technical Analysis --
# After displaying the information found on the job's webpage in Initial Analysis, I found that the job's HTML link is as follows:
# <a href="https://www.timesjobs.com/job-detail/android-developer-seven-consultancy-navi-mumbai-mumbai-thane-2-to-5-yrs-jobid-t2sYavWXWjVzpSvf__PLUS__uAgZw==&amp;source=srp" target="_blank" onclick="logViewUSBT('view','70767301','java  ,  mobile  ,  mobile application development','Navi Mumbai,  Mumbai,  Thane','2 - 5','IT Software : Software Products &amp; Services','1','' )" class="posoverlay_srp"></a>class="posoverlay_srp"></a>

# The information containing the Job Title, Company Name, and Date Posted is under <header class="clearfix">
# The Company Name and Date Posted is separated in <div class="d-flex d-flex-align-item">

# -- Locations --
# Company Name is located under <h3 class="joblist-comp-name"> SEVEN CONSULTANCY </h3>
# Job Title is located under <h2 class="heading-trun" title="Android Developer">
# Date Posted is located under <span class="sim-posted"> ::before <span>few days ago</span>

# Key skills are located under
# <div class="more-skills-sections">
# <span>java</span> 
# <span>mobile</span> 
# <span>mobile application development</span> 
# </div>

# -------------------------------------------------------------------------------------------------------------------------------------------

# Link to the webpage
html_link = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=%22Mobile+Application+Development%22%2C&cboWorkExp1=2&txtLocation='

html_request = requests.get(html_link)

# Confirm a successful connection was made
# If successful, <Response [200]> will be printed
print(html_request)

# HTML file content from timesjobs.com
html_text = requests.get(html_link).text

# Create an instance of BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')


# -------------------------------------------------------------------------------------------------------------------------------------------

# Section 1 - Analyzing the Most Recent Job

print ("\n__________\n")
print ("Section 1 - Analyzing the Most Recent Job")
print ("\n__________\n")

# My Output for this section:
# Job Title: Android Developer
# Company Name: Seven Consultancy
# Date Posted: Few Days Ago
# Skills: Java, Mobile, Mobile Application Development

# Find the first job posted
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')

# Grab the Job Title
title_header = job.find('h2', class_ = 'heading-trun')
job_title = title_header['title'].title()

# Grab the Company Name
company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().title()

# Grab the Date Posted
date_posted = job.find('span', class_='sim-posted').text.strip().title()

# Grab the skills
# Find the div containing the skills
skills_div = job.find('div', class_='more-skills-sections')
# Loop through all the skills
skills = [span.text.strip() for span in skills_div.find_all('span')]
skills = ", ".join(skills).title()

# Print all findings
print(f"Job Title: {job_title}")
print(f"Company Name: {company_name}")
print(f"Date Posted: {date_posted}")
print(f"Skills: {skills}")


# -------------------------------------------------------------------------------------------------------------------------------------------

# Section 2 - Analyzing the Job List (Page 1)
# Since the Job postings are separated by pages (more webpages, updated dynamically of course),
# I'm analyzing the first page (landing page when you search) in this section of code.

print ("\n__________\n")
print ("Section 2 - Analyzing the Job List (Page 1)")
print ("\n__________\n")

# My Output for this section:

# Find all the jobs on the page
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

# Loop through all the jobs
for job in jobs:
  # Grab the Job Title
  title_header = job.find('h2', class_ = 'heading-trun')
  job_title = title_header['title'].title()

  # Grab the Company Name
  company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().title()

  # Grab the Date Posted
  date_posted = job.find('span', class_='sim-posted').text.strip().title()

  # Grab the skills
  # Find the div containing the skills
  skills_div = job.find('div', class_='more-skills-sections')
  # Loop through all the skills
  skills = [span.text.strip() for span in skills_div.find_all('span')]
  skills = ", ".join(skills).strip().title()

  # Print all findings
  print(f"Job Title: {job_title}")
  print(f"Company Name: {company_name}")
  print(f"Date Posted: {date_posted}")
  print(f"Skills: {skills}\n")