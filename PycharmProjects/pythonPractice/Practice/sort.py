"""
输入三个整数x,y,z，请把这三个数由小到大输出。

"""

#方法一：排序算法实现
raw=[]
for i in range(3):
    x=int(input('int%d:' %(i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)


#方法二：调用sort函数排序
raw2=[]
for i in range(3):
    x=int(input('int%d:' %(i)))
    raw2.append(x)
print(sorted(raw2))