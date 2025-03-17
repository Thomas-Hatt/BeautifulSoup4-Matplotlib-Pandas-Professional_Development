# pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - Read Data - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# Links to each program
dfLinks = pd.read_csv('programs.csv', usecols=[0])

# Each Program Title (for example, Computer Information Systems, A.A.S.)
dfNames = pd.read_csv('programs.csv', usecols=[1], names=['Program'], header=None)

# -------------------------------------------------------------------------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - -  Program Categories - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# Categorize programs
def categorize_program(program):
  program_lower = program.lower()
  if 'certificate' in program_lower:
    return 'Certificate'
  elif 'a.a.s' in program_lower:
    return 'A.A.S'
  elif 'associate in' in program_lower:
    return 'Associate'
  else:
    return 'N/A'

dfNames['Category'] = dfNames['Program'].apply(categorize_program)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - -  Field Categories   - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# Create a dictionary to store the respective fields with their keywords
field_map = {
    'Technology': ['Technology', 'IT', 'Cybersecurity', 'CAD', 'Mechatronics'],
    'Health': ['Nursing', 'Dental', 'Therapist', 'Health Fitness', 'Paramedics'],
    'Business': ['Business', 'Accounting', 'Marketing', 'Entrepreneurship'],
    'Arts': ['Art', 'Design', 'Music', 'Photography'],
    'Trades': ['Welding', 'Automotive', 'HVAC', 'Construction']
}

# Loop through each field for keywords
# If no keywords are found that are associated in field_map, return 'Other'
def categorize_field(program):
  for field, keywords in field_map.items():
    if any(keyword.lower() in program.lower() for keyword in keywords):
      return field
  return 'Other'

# Applies categorize_field to every row in the Program column of the dfNames DataFrame
dfNames['Field'] = dfNames['Program'].apply(categorize_field)

# -------------------------------------------------------------------------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - Visualization functions - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# --- Categories of Programs of Study (A.A.S, Associate, Certificate, or N/A) --- #
def plot_program_categories():
  # Create a dictionary to store the respective programs of study with a hexcode
  color_map = {
    'Certificate': '#1f77b4',
    'A.A.S': '#4d99f0',
    'Associate': '#00c2ff',
    'N/A': '#A7C7E7'
  }

  # Count the number of occurences in the category column of the dfNames DataFrame
  counts = dfNames['Category'].value_counts()

  # Assign colors to each category
  colors = [color_map[label] for label in counts.index]

  # 8 x 6 pie chart  
  plt.figure(figsize=(8, 6))
  plt.pie(
    counts, # Visualize the number of programs in each category
    labels=counts.index, # Sets the labels for each pie slice to the category names
    colors=colors, # Assign the list of colors
    autopct='%1.1f%%', # Displays the percentage of each slice with one decimal place
    startangle=90, # Rotates the pie chart so it starts at 90°
    wedgeprops={'edgecolor': 'white'}) # Adds white edges to the slices for better visual clarity

  # Create title of graph
  plt.title('Distribution of Program Categories')

  # Display graph
  plt.show()


# --- Field Distribution (Technology/Health/Business/etc) --- #
def plot_field_distribution():
  # 6 x 5 pie chart 
  plt.figure(figsize=(6, 5))
  dfNames['Field'].value_counts().plot(kind='pie', autopct='%1.1f%%', colormap='Greens')
  
  # Create title of graph
  plt.title('Program Distribution by Field')

  # Display graph
  plt.show()


# --- View Top 10 Program Keywords ---
def top_keywords():
  # Extract words from program names
  words = dfNames['Program'].str.lower().str.replace(r'[^\w\s]', '', regex=True)
  words = words.str.split(expand=True).stack()

  # Get rid of common words that aren't helpful for analysis
  stopwords = {'and', 'in', 'of', 'a.a.s.', 'certificate', 'associate', 'aas', 'general'}
  filtered_words = words[~words.isin(stopwords)]

  # Count word frequencies
  word_counts = Counter(filtered_words)

   # Get top 10 most common words
  top_words = pd.Series(word_counts).nlargest(10)

  # Create a horizontal bar chart
  plt.figure(figsize=(12, 8)) # 12 x 8 horizontal bar chart
  top_words.sort_values().plot(kind='barh', color='skyblue', edgecolor='black')

  # Add chart title and labels
  plt.title('Top 10 Most Common Keywords in Program Names', fontsize=16)
  plt.xlabel('Frequency', fontsize=14)
  plt.ylabel('Keywords', fontsize=14)

  # Add gridlines for better readability
  plt.grid(axis='x', linestyle='--', alpha=0.5)

  # Display the chart
  plt.tight_layout()
  plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - -  Main Function/Menu   - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# User interface
def show_menu():
  while True:
    print("\nChoose a visualization:")
    print("1. Program Categories (A.A.S/Certificate/Associate)")
    print("2. Field Distribution (Technology/Health/Business/etc)")
    print("3. View Top 10 Program Keywords")
    print("99. Exit")
        
    # User Input    
    choice = input("Enter your choice: ")
        
    # Program Categories (A.A.S/Certificate/Associate)    
    if choice == '1':
      plot_program_categories()

    # Field Distribution (Technology/Health/Business/etc)  
    elif choice == '2':
      plot_field_distribution()

    # 3. View Top 10 Program Keywords
    elif choice == '3':
      top_keywords()

    # Exit program  
    elif choice == '99':
      print("Exiting program...")
      break
    else:
      print("Invalid input. Please enter 1, 2, 3, or 99.")

# Start the program
if __name__ == "__main__":
  show_menu()