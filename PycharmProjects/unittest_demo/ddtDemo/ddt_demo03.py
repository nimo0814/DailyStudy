#使用 “@data+@unpack” 输入简单测试数据
import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class myddt(unittest.TestCase):
    @data([2,3],[4,5])
    @unpack
    def test_a(self,first,second):
        print("first:",first)
        print("second:",second)

if __name__=='__main__':
    unittest.main()