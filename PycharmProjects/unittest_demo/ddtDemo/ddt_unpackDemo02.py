import unittest
from ddt import ddt,data,unpack

def add(a,b):
    return a+b
@ddt
class MyTest(unittest.TestCase):
    @data([1,2,3],[1,0,1],[0,0,0],[1,1,3])#依次传递列表
    @unpack
    def test(self,a,b,c):
        print(a,b,c)
        if a+b==c:
            print(True)
        else:
            print(False)

if __name__=='__main':
    unittest.main(verbosity=2)