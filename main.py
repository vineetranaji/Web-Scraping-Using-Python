import xlrd
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
conn = sqlite3.connect('projectdb.db')
conn.execute("""CREATE TABLE IF NOT EXISTS DATA
          (WEBPAGE TEXT NOT NULL,
          WORD TEXT NOT NULL,
          COUNT INT NOT NULL)""")
def get_words(x):                         #creating a function for doing hte desired task
  file = '/Users/vineet/Desktop/Project/test.xlsx'             #test.xlsx is the workbook containing the webpages and words to search for,please change location of file
  wb = xlrd.open_workbook(file)              #OPEN WORKBOOK
  sheet = wb.sheet_by_index(x)
  url_list = []
  word_list = []
  i = 0
  url = sheet.cell_value(0,0)
  while True:
    try:
      word = sheet.cell_value(i,1)
    except IndexError:
      break
    else:
      word_list.append(word)
      i+=1
  file_handle = urlopen(url)
  html = file_handle.read()
  soup = BeautifulSoup(html,"html.parser")
  for script in soup(["script","style"]):                 #to remove all js notations and html tags from script
    script.extract()
  text_list = (soup.get_text()).split()
  for words in word_list:
    conn.execute("INSERT INTO DATA(WEBPAGE,WORD,COUNT) VALUES (?,?,?)",(url,words,text_list.count(words)))  #putting in database
  conn.commit()
  print("Processing...")
index = 0
while True:
  try:
    get_words(index)
  except IndexError:                              #EXECUTION IS HERE
    break
  else:
    index+=1
print("Finished")

