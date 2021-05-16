"""
练习函数调用
"""
def hello_runboo():
    print('RUNOOB')
def hello_runboos():
    for i in range(3):
        hello_runboo()

if __name__=='__main__':
    hello_runboos()