import openpyxl

wb=openpyxl.load_workbook('Book2.xlsx')
print(wb.sheetnames)#获取工作簿中的表（列表）
print(wb.active)#获取当前活跃的worksheet
print(wb.worksheets)#以列表的形式返回所有的worksheet
print(wb.read_only)#判断是否以read_only模式打开excel文档
print(wb.encoding)#获取文档的字符集编码
print(wb.properties)#获取文档的元数据，如标题，创建者，创建日期等