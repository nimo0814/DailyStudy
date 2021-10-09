#传递json文件
import unittest
from ddt import ddt,file_data
def add(a,b):
    return a+b

@ddt
class MyTest(unittest.TestCase):
    @file_data("test.json")
    def test(self,a,b,c):
        print(a,b,c)

if __name__=='__main__':
    unittest.main(verbosity=2)