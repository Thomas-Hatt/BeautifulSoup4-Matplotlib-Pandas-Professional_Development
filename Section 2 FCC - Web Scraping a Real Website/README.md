# Web Scraping Job Postings with Python and Beautiful Soup

This project focuses on web scraping dynamic job postings from the [TimesJobs](https://www.timesjobs.com/) website using Python and the Beautiful Soup library. The code demonstrates how to extract details about job titles, company names, posting dates, and required skills. This project is based on the **Beautiful Soup Crash Course** tutorial by freeCodeCamp.org.

---

## Overview

The project provides:
1. **Analysis of the Most Recent Job Post:** Extracts details such as job title, company name, posting date, and required skills from the most recent job listing on the first page.
2. **Analysis of the Full Job List (Page 1):** Iterates through all job postings on the first page and extracts relevant information.

This script is designed to work with the TimesJobs website as of **March 15, 2025**, and may require updates if the website's structure changes in the future.

---

## Requirements

To run this project, you'll need:
- Python (version 3.6 or higher recommended, I used version 3.13.2).
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`

Install the required libraries using pip:

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
```

## How It Works

I did an initial analysis and a technical analysis, where I observed how the webpage looks, as well as the code that makes up what you're viewing on screen. I searched for "Mobile Application Development".

Here are the findings from my analyses:
### -- Initial Analysis (Plain Text) --
Job posted by SEVEN CONSULTANCY

Industry: IT-Software

Specialization: Mobile

Qualification: Any Graduate

Job title is "Android Developer"

Job Location is "Navi Mumbai (Maharashtra), Mumbai (Maharashtra), Thane (Maharashtra)"

Job Function: IT Software : Software Products & Services

Employment Type: Full Time

Key Skills - java, mobile, mobile application development

### -- Initial Technical Analysis --
All of the main content, including job postings, are under ```<div class="inside-rhs main-search-block">```

It is then separated by ```<div id="searchResultContents">```

The joblist is displayed in an unordered list ```<ul class="new-joblist">```

Each job posting is an object in the list categorized by ```<li class="clearfix job-bx wht-shd-bx">```

### -- Further Technical Analysis --
After displaying the information found on the job's webpage in Initial Analysis, I found that the job's HTML link is as follows:

```<a href="https://www.timesjobs.com/job-detail/android-developer-seven-consultancy-navi-mumbai-mumbai-thane-2-to-5-yrs-jobid-t2sYavWXWjVzpSvf__PLUS__uAgZw==&amp;source=srp" target="_blank" onclick="logViewUSBT('view','70767301','java  ,  mobile  ,  mobile application development','Navi Mumbai,  Mumbai,  Thane','2 - 5','IT Software : Software Products &amp; Services','1','' )" class="posoverlay_srp"></a>```

The information containing the Job Title, Company Name, and Date Posted is under <header class="clearfix">
The Company Name and Date Posted is separated in <div class="d-flex d-flex-align-item">

### -- Locations --

Company Name is located under ```<h3 class="joblist-comp-name"> SEVEN CONSULTANCY </h3>```
Job Title is located under ```<h2 class="heading-trun" title="Android Developer">```
Date Posted is located under ```<span class="sim-posted"> ::before <span>few days ago</span>```

Skills is located under
```
<div class="more-skills-sections">
<span>java</span> 
<span>mobile</span> 
<span>mobile application development</span> 
</div>
```

## Notes
Since this website is dynamically updated to show new jobs as they are uploaded, my code, comments, and analyses cannot accurately reflect how it is at a future date. The date that I am analyzing this on is March 15th, 2025.

It is also possible that the structure of the HTML webpage could change in the future (which would render this code unusable), since it has changed since the original YouTube video upload date of November 18th, 2020.

## Example Output

After running my code (as of 3/15/2025, since the website is dynamically updated), here is the output of my scraped data:

```
<Response [200]>

__________

Section 1 - Analyzing the Most Recent Job

__________

Job Title: Android Developer
Company Name: Seven Consultancy
Date Posted: Few Days Ago
Skills: Java, Mobile, Mobile Application Development

__________

Section 2 - Analyzing the Job List (Page 1)

__________

Job Title: Android Developer
Company Name: Seven Consultancy
Date Posted: Few Days Ago
Skills: Java, Mobile, Mobile Application Development

Job Title: React Native
Company Name: Vocso Technologies
Date Posted: Few Days Ago
Skills: Mobile Application Development, Ios, Android Platform

Job Title: Ionic Developer
Company Name: Evince Technologies
Date Posted: Few Days Ago
Skills: Mobile Development, Mobile, Mobile Application Development

Job Title: Iphone Developer
Company Name: D-Amies Technologies Pvt. Ltd.
Date Posted: Few Days Ago
Skills: Iphone Developer, Ios, Mobile Application Development

Job Title: Andriod App Developer
Company Name: Spark Infosystems
Date Posted: Few Days Ago
Skills: Mobile, Mobile Application Development, Ios, Windows Mobile, Symbian

Job Title: Android Mobile App Developer
Company Name: Spark Infosystems
Date Posted: Few Days Ago
Skills: Mobile, Mobile Application Development, Ios, Windows Mobile, Symbian

Job Title: Android Developer
Company Name: Myupchar
Date Posted: Posted 2 Days Ago
Skills: Android Sdk, Reports, C, Software Development, C, Mobile, Application Development, Java, Android Developer

Job Title: Information Security Officer
Company Name: Indifi Technologies Pvt Ltd
Date Posted: Few Days Ago
Skills: Application Performance, Memory Management, Java, Design Patterns, Data Structures, Mvp, Mobile, Application Development, Threading

Job Title: Ios Developer
Company Name: Maraekat Infotech Ltd.
Date Posted: Few Days Ago
Skills: Objective C, Ios Developer, Ios, Xcode, Mobile Application Development, Cocoa, Swift

Job Title: Android Developer
Company Name: Technomobs It Solutions-Ajman Uae
Date Posted: Few Days Ago
Skills: Information Technology, Software Engineering, Mobile Application Development, Ios, Mobile Application Developer

Job Title: React Native Intern
Company Name: 3Ri Technologies Pvt Ltd
Date Posted: Few Days Ago
Skills: Mobile Application Development, React Native Framework, Javascript Programming, Problem Solving Techniques, Team Collaboration

Job Title: Mobile Application Developer
Company Name: Cyberindigo Net Private Limited
Date Posted: Few Days Ago
Skills: Os, Mobile, Mobile Application Development, Mobile Application Developer, Iphone, Symbian, Written Communication, Windows Mobile

Job Title: Android / Ios Developer  (  81144431  )
Company Name: Reliance Jio Infocomm Limited
Date Posted: Few Days Ago
Skills: Mobile Framework Experience, Android  /  Ios Systems, Object Oriented Programming, System Integration, Application Development, System Analysis, Mobile Application Development

Job Title: Android Developer
Company Name: Itsws Technologies Pvt. Ltd.
Date Posted: Few Days Ago
Skills: Android Sdk, Web Services, Coding, Database, Java, Xml Parsing, Software Development, Sqlite, Mvp, Android Studio, Mobile, Application Development, Android Developer

Job Title: Director ,  Software Engineering
Company Name: Mastercard
Date Posted: Few Days Ago
Skills: Product Engineering, Microservice Architecture, Restful Apis, Mobile Application Development, Project Management, Security, Software Engineering, Web Development, Director

Job Title: Jd-Ios Developer
Company Name: Vst Mobility Solutions
Date Posted: Few Days Ago
Skills: Hosting, Storage, Mobile Application Development, Ios, Objective C, Ios Sdk, Swift, Ios Developer, Mobile, Xcode, Mobile Application Developer

Job Title: Ios Developer
Company Name: Kirusa
Date Posted: Few Days Ago
Skills: Ios, Mobile Application Development, Objective C, Java, Linux, Data Structures, Ios Developer, Mobile, Xcode, Mobile Application Developer, Cocoa Touch

Job Title: Director ,  Software Engineering
Company Name: Mastercard
Date Posted: Few Days Ago
Skills: Api Development, Microservice Architecture, Mobile Application Development, Project Management, Strategic Leadership, Security, Software Engineering, Web Development, Director

Job Title: Advanced Application Engineer
Company Name: Accenture
Date Posted: A Month Ago
Skills: Fluent Commerce Functional, Fluent Commerce Technical, Modular Architectures, Agile Methodologies, Cross Functional Collaboration, Software Development, Mobile, Application Development

Job Title: Senior Software Architect
Company Name: Ge Healthcare Ltd
Date Posted: Few Days Ago
Skills: C   Programming, Microservices Architecture, Software Design Patterns, Cloud Based Solutions, Mobile Application Development, Mentor, Web Services, Unit Testing, Software Architect, Data Structures, Enterprise Security, Mentoring, Coding, Dicom

Job Title: Software Engineer Ii
Company Name: Microsoft India Pvt Ltd
Date Posted: Few Days Ago
Skills: Mobile Application Development, Multi Factor Authentication, Coding Best Practices, Test Automation, Team Collaboration, C, Security, Java, Software Engineer, Software Engineering, C#, San, Python, Javascript, Livesite

Job Title: React Native Developer
Company Name: Webiots
Date Posted: Few Days Ago
Skills: React Native Development, Mobile Application Development, React Principles, Ui  /  Ux Design, Restful Apis, Css, Information Technology, Javascript, React.Js, Web Technologies, Debugging, Html

Job Title: Associate Architect
Company Name: Myntra
Date Posted: Few Days Ago
Skills: Software Architecture Design, Cloud Service Development, Big Data Analytics, Mobile Application Development, Distributed Systems Engineering, Fundamentals, Security, Database, Java, Devops, Rdbms, Imaging, Nosql, Messaging

Job Title: Senior Software Engineer - Frontend
Company Name: Myntra
Date Posted: Few Days Ago
Skills: Mobile Application Development, Ui Architecture Design, Frontend Coding Standards, Cross Functional Collaboration, Responsive Layout Building, Css, Html5, Senior Software Engineer, Imaging, Javascript

Job Title: Software Engineer Ii
Company Name: Microsoft
Date Posted: Few Days Ago
Skills: Native C  /  C   Development, Mobile Application Development, Strong Debugging Skills, Performance Optimization, Analytical Problem Solving, Fundamentals, Security, Java, Software Engineer, C#, Python, Javascript, Written Communication
```