import openpyxl

if __name__=='__main__':
    path ='/Users/daiyali/PycharmProjects/unittest_demo/data/test_cases.xlsx'
    #读取excel文件
    workbook = openpyxl.load_workbook(path)
    #读取所有sheet
    sheet=workbook.get_sheet_names()
    #获取某个sheet
    sheet=workbook[sheet[0]]
    print(sheet)
    #获取某个cell的值
    cell_val=sheet.cell(row=2,column=2).value
    print(cell_val)