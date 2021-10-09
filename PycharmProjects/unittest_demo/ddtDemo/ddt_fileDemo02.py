#传递多层json文件
import unittest
from ddt import ddt,file_data
def add(a,b):
    return a+b

@ddt
class MyTest(unittest.TestCase):
    @file_data("test2.json")
    def test(self,data,result):
        print(data,result)

if __name__=='__main__':
    unittest.main(verbosity=2)