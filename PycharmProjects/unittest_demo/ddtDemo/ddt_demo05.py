import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class myddt(unittest.TestCase):
    @file_data('/Users/daiyali/PycharmProjects/unittest_demo/ddtDemo/yaml_write.yaml')
    def test_a(self,value):
        print(value)
if __name__=='__main__':
    unittest.main()

