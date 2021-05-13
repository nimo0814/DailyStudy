"""
题目 将一个整数分解质因数。例如：输入90,打印出90=233*5。
程序分析 根本不需要判断是否是质数，从2开始向数本身遍历，能整除的肯定是最小的质数。
"""
"""
target=int(input('输入一个整数：'))
print(target,'= ',end='')
if target<0:
    target=abs(target)
    print('-1*',end='')
flag=0
if target<=1:
    print(target)
    flag=1

while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i,end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target/=i
            break
"""
#方法二：

def reduceNum(n):
    print('{}='.format(n),end="")
    if not isinstance(n,int) or n<=0:
        print('请输入一个正确的数字！')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        for index in range(2,n+1):
            if n%index==0:
                n//=index
                if n==1:
                    print(index)
                else:
                    print('{}*'.format(index),end=" ")
                break
number=int(input("请输入数字："))
reduceNum(number)