# Web-Scraping-Using-Python
Overview
This project demonstrates a comprehensive data processing workflow using Python. It involves web scraping, word counting, storing data in an SQLite database, and exporting the processed data to an Excel file. The primary goal is to count the occurrences of specific words on various web pages and store this data in a structured format.

Project Components
Web Scraping, Data Fetching and Processing:
Reads URLs and words from an Excel file.
Fetches HTML content from each URL.
Cleans and parses the HTML content using BeautifulSoup.
Counts the occurrences of specified words.
Stores the results in an SQLite database.

Data Export:
Retrieves the stored data from the SQLite database.
Writes the data into an Excel file, organizing it into multiple sheets based on unique webpage entries.

Detailed Steps
1. Setup and Imports
The project starts by importing the necessary libraries:

xlrd for reading Excel files.
xlwt for creating and writing to Excel files.
sqlite3 for interacting with the SQLite database.
urllib.request for fetching web content.
BeautifulSoup from bs4 for parsing HTML content.

2. Database Connection and Table Creation
We establish a connection to an SQLite database named projectdb.db. If the table DATA does not already exist, it is created with columns for the webpage URL, word, and word count.

3. Defining the get_words Function
The get_words function handles reading the Excel file, fetching web content, cleaning and parsing HTML, and counting word occurrences. It also stores the results in the SQLite database.

4. Fetching and Storing Data
We use a loop to call the get_words function for each sheet in the Excel file until all sheets are processed.

6. Exporting Data to Excel
After processing and storing the data in the SQLite database, we retrieve the data and write it into an Excel file. The data is organized into multiple sheets, each representing a unique webpage.

Conclusion
This project showcases a full data processing pipeline from web scraping to database storage and final data export into an Excel file. By integrating different Python libraries, we efficiently manage and process data, demonstrating a robust workflow for similar tasks.
