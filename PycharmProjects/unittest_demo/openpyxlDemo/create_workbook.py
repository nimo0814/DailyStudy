import openpyxl
wb=openpyxl.Workbook('Book1.xlsx')
wb1=openpyxl.load_workbook('Book2.xlsx')

print(wb)
print(type(wb))
print(wb1)
print(type(wb1))