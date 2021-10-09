import unittest
from ddt import data,unpack,ddt
@ddt
class myddt(unittest.TestCase):
    @data("123")#单个值
    def test1(self,testdata1):
        print(testdata1)
        print("-------------------")
    @data([1,2,3],[4,5,6]) #列表
    def test2(self,testdata2):
        print(testdata2)
        print("-------------------")
    @data((1,2,3)) #元祖
    def test3(self,testdata3):
        print(testdata3)
        print("-------------------")
    @data({'zhangsan':1,'wangwu':2,'lisi':3}) #字典
    def test4(self,testdata4):
        print(testdata4)
        print("-------------------")
if __name__=='__main__':
    unittest.main()

