import xlwt            # i an using xlwt instead of xlsxwriter as it was easier
import sqlite3
conn = sqlite3.connect('projectdb.db')  
workbook= xlwt.Workbook()
c=conn.cursor()           #connecting to database
c.execute("SELECT WEBPAGE,WORD,COUNT FROM DATA")    
final  = c.fetchall()
i = 0
j = 0
sheet = workbook.add_sheet("Sheet1")
ctr = 2
while True:
  row = 0
  col = 0
  try:
    web = final[i][j]
  except IndexError:
    break
  else:
    sheet.write(0,0,web)
  while True:
    try:
      if web!= final[i][j]:
        break
      sheet.write(row,col+1,final[i][j+1])
      sheet.write(row,col+2,final[i][j+2])
    except IndexError:
      break
    else:
      row+=1
      i+=1
  s = "Sheet"
  s = s + str(ctr)
  sheet = workbook.add_sheet(s)
  ctr+=1
print("Done")
workbook.save("Project.xls")       #saving the workbook
