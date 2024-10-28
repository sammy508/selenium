
import openpyxl

file = r"D:\selenium projects\selenium\1st-proj OrangeHRM\Data driven testing\datawritten.xlsx"
workbook= openpyxl.load_workbook(file)

sheet = workbook.active  # it works on active sheet and best for single sheet

for row in range(1, 5):
    for col in range(1, 4):
        sheet.cell(row=row, column=col).value = "practice data "
      
workbook.save(file)        
