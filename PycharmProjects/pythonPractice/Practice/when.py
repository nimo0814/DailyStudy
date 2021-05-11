"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
#判断是否为闰年
def isLeapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))
DofM=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input('Year:'))
month=int(input('Month:'))
day=int(input('Day:'))
if isLeapYear(year):#如果是闰年，二月份需要加一天
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
print(res+day)