# pip install pandas

from bs4 import BeautifulSoup
import requests
import pandas as pd

# The purpose of this file is to grab all of the programs of study and their respective links, and combine them into a CSV file to be read in main.py

# -------------------------------------------------------------------------------------------------------------------------------------------
# Main webpage (shows Associate Degrees, Certificates, and Alternative Training)
main_url = "https://catalog.mcc.edu/content.php?catoid=17&navoid=518"

# Combining the <a href> tag needs to be done with the base url, so I initialized a variable for that
base_url = "https://catalog.mcc.edu"

html_request = requests.get(main_url)

# Confirm a successful connection was made
# If successful, <Response [200]> will be printed
print(html_request)

# HTML file content from MCC's catalog webpage
html_text = requests.get(main_url).text

# Create an instance of BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')

# -------------------------------------------------------------------------------------------------------------------------------------------

# -- Initial Analysis --

# - All links for Associate Degrees, Certificates, and Alternative Training Programs are under the "Programs of Study" header
# - All Associate Degrees have a smaller header with the words "Associate in " following the Associate Degree Category
# - Each individual Associate Degree is located in a list under the category

# - All Certificates are located in a list under the sub heading "Certificate" and end with the word "Certificate"

# - All Alternative Training Programs are located in a list under the sub heading "Alternative Training"

# -------------------------------------------------------------------------------------------------------------------------------------------

# -- Initial Technical Analysis --
# It appears that the whole webpage is located under <table class="toplevel table_default">
# It further condenses down to <table class="block_n2_and_content table_default">

# All of the Programs of Study are located under <table class="table_default"> and <td class="block_content" colspan="2">

# Each subheading is displayed similar to 
# <p style="padding-left: 30px"><strong>Associate in Science</strong></p>

# Each link to each individual Program of Study is displayed similar to 
# <ul class="program-list">
# <li style="list-style-type: none">•&nbsp;
# <a href="preview_program.php?catoid=17&amp;poid=2034&amp;returnto=518">Associate in Science</a></li>
# </ul>

# -------------------------------------------------------------------------------------------------------------------------------------------



# Extract all program links and their text from the "program-list" sections
program_links = []
for link in soup.select('ul.program-list a[href]'):
  # Get the link of each program
  href_text = link['href']

  # Combine the program link with the base URL
  full_url = base_url + "/" + href_text + ","

  # Get the text within the <a> tag and remove any leading/trailing whitespace
  link_text = link.text.strip()

  # Add the program name with the course link to the array index
  program_links.append((full_url, link_text))

  # Display each program name with their link
  print(f"Found link: {link_text} - {full_url}")

# Convert the array into a CSV file using pandas
df = pd.DataFrame(program_links, columns=['URL,', 'Program'])

# Replace commas with spaces in the 'Program' column
df['Program'] = df['Program'].str.replace(',', '')

# Replace "AAS" with "A.A.S" in the 'Program' column
df['Program'] = df['Program'].str.replace('AAS', 'A.A.S')

# Save to CSV. There should be 97 total links as of 3/16/2025
df.to_csv('programs.csv', index=False, sep=' ')