import openpyxl
wb=openpyxl.load_workbook('Book2.xlsx')
#选择要操作的工作表，返回工作表对象
sheet=wb['test1']
for row in sheet.rows:
    for cell in row:
        print(cell.value,end=',')
    print()