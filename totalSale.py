from os import listdir
from xlrd import open_workbook 

mypath = "C:\\Users\\iukha\\OneDrive\\Documents\\Gameplay Sales\\April 2019"
sum = 0
for file in listdir(mypath):
    if file.endswith(".xlsx"):
        wb = open_workbook(mypath+"\\"+file)
        print(file)
        sheet = wb.sheet_by_index(0) 
        cell = sheet.cell(rowx=0, colx=9).value
        print(cell)
        sum += int(cell)
print(sum)
