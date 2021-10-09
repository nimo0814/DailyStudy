#使用"@data"输入简单测试数据
import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class myddt(unittest.TestCase):
    @data(1,2,3)
    def test_a(self,value):
        print(value)

if __name__=='__main__':
    unittest.main()