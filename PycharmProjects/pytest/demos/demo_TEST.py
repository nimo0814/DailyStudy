import pytest
class TestDemo:
    def testlogin(self,global_fixture):
        print('ok,'+global_fixture)
    def test_logout(self):
        print('logout')
