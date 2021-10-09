#使用 “@file_data” 输入json格式测试数据（除了以“.yml”和“.yaml”结尾的文件，其它的都会被默认为json格式的文件）
import unittest
from ddt import ddt,data,file_data,unpack
@ddt
class myddt(unittest.TestCase):
    @file_data('/Users/daiyali/PycharmProjects/unittest_demo/ddtDemo/schoolDetail.json')
    def test_a(self,*key,**value):
        print(key,value)

if __name__=='__main__':
    unittest.main()



