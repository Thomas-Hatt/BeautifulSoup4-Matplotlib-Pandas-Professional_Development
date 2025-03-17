# Web Scraping with Python - Beautiful Soup Crash Course by freeCodeCamp.org
# Link to the YouTube video - https://www.youtube.com/watch?v=XVv6mJpFOb0
# Link to the GitHub page with extra sample files - https://github.com/jimdevops19/codesnippets/tree/main/Python%20Web%20Scraping

from bs4 import BeautifulSoup

# Open a file and then read the contents of the file
with open('home.html', 'r') as html_file:
  content = html_file.read()

# Initialize an instance of BeautifulSoup
  soup = BeautifulSoup(content, 'lxml')

# -------------------------------------------------------------------------------------------------------------------------------------------

# Section 1 - Print All Contents of the HTML File
  print ("\n__________\n")
  print ("Section 1 - Print All Contents of the HTML File")
  print ("\n__________\n")

  # Print the contents of the HTML file
  print(content)
    # Outputs -- all of the code within home.html

# -------------------------------------------------------------------------------------------------------------------------------------------


  # Section 2 - Print All <h5> Tags
  print ("\n__________\n")
  print ("Section 2 - Print All <h5> Tags")
  print ("\n__________\n")

  # Search for the <h5> tags within the HTML file
  courses_html_tags = soup.find_all('h5')

  # Print the tags
  print(courses_html_tags)
    # Outputs --
      # [<h5 class="card-title">Python for beginners</h5>, <h5 class="card-title">Python Web Development</h5>, <h5 class="card-title">Python Machine Learning</h5>]


# -------------------------------------------------------------------------------------------------------------------------------------------

  # Section 3 - Prettier <h5> Tag Printing
  print ("\n__________\n")
  print ("Section 3 - Prettier <h5> Tag Printing")
  print ("\n__________\n")

  # Loop through all of the courses (<h5> tags)
  for course in courses_html_tags:

    # Print the tags
      print(course.text) 
        # Outputs --
          # Python for beginners
          # Python Web Development
          # Python Machine Learning

# -------------------------------------------------------------------------------------------------------------------------------------------

  # Section 4 - Print Course Title and Course Price
  print ("\n__________\n")
  print ("Section 4 - Print Course Title and Course Price")
  print ("\n__________\n")


  # For this section, we're looking for the part of the HTML webpage that says "Start for XX$"

  # Each course is located under a div with the class of "card"
  course_cards = soup.find_all('div', class_='card')

  # Loop through the courses
  for course in course_cards:

    # Each course title is under an <h5> tag
    # For example, <h5 class="card-title">Python for beginners</h5>
    course_title = course.h5.text

    # Each course price is under an <a href="#"> tag
    # For example, <a href="#" class="btn btn-primary">Start for 20$</a>
    # Split the text for course price and get the last element
    course_price = course.a.text.split()[-1]

    # Print our findings
    print(f'{course_title} costs {course_price}')
      # Outputs --
        # Python for beginners costs 20$
        # Python Web Development costs 50$
        # Python Machine Learning costs 100$