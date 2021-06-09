import pytest

class TestDemo:
    #定义一个fixture方法
    @pytest.fixture(scope='class')
    def normal(self):
        print('normal')
        return 99
    #在这个测试方法中通过参数形式调用fixture
    #如果fixture有返回值的话，可以直接使用fixture的返回值
    def testlogin(self,normal):
        print("====testlogin====")
        assert normal==99

    def test_logout(self,normal):
        print('logout')
        print(normal)

if __name__=='__main__':
    pytest.main(['-s','demo01_TEST.py'])
