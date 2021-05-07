from test_practice.caculator import Count
#测试两个数相加
class TestCount:

    def test_add(self):
        try:
            j=Count(2,3)
            add=j.add()
            assert (add==5),'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('Test pass')
#执行测试类的方法
mytest=TestCount()
mytest.test_add()