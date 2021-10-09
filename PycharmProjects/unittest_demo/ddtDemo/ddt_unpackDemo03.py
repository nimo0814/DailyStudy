import unittest
from ddt import ddt,data,unpack

def add(a,b):
    return a+b
@ddt
class MyTest(unittest.TestCase):
    @data({"a":1,"b":1,"c":2},{"a":-1,"b":1,"c":0},{"a":0,"b":0,"c":0})#依次传递字典
    @unpack
    def test(self,a,b,c):
        print(a,b,c)
        if a+b==c:
            print(True)
        else:
            print(False)

if __name__=='__main':
    unittest.main(verbosity=2)