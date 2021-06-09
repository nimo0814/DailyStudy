import pytest
namelist=['zhangsan','lisi','wangwu']

@pytest.fixture(params=namelist,autouse=True)
def myfixture(request):
    return request.param

class TestDemo:
    def testlogin(self,myfixture):
        print("====testlogin====")
        print(myfixture)
    def test_logout(self):
        print('logout')

if __name__=='__main__':
    pytest.main(['-s','demo02_TEST.py'])