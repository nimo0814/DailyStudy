import unittest
import ddt

data=[
    (1,2,3),
    (1,3,4),
    (1,4,5)
]

@ddt.ddt
class IntegerArithmeticTestCase(unittest.TestCase):
    #多组数据，@ddt.data(*data)相当于@ddt.data((1,2,3),(1,3,4),(1,4,5))
    @ddt.data(*data)
    #每次运行都会从data中取出一组数据，动态生成一个独立的测试用例方法
    def testAdd(self,test_data):
        print(test_data)
        self.assertEqual((test_data[0]+test_data[1]),test_data[2])
    '''测试用例方法名生成规则
    使用ddt后，会产生一个新的测试用例方法名：之前的测试用例方法名_ordinal_data
    之前的测试用例方法名：即定义的测试用例方法名。比如def test_large（），这里就是test_large
    ordinal：整数，从1开始递加
    data：如果传递过来的数据存在__name__属性，则这里就是该数据的__name__值。如果未定义__name__属性，ddt会尽量将传递过来的
    数据转换成python标识符，作为data显示。比如（3，2）就转换为3_2.需要注意的是如果数据是字典，则这里就是字典的key
    '''
if __name__=='__main__':
    unittest.main(verbosity=2)
