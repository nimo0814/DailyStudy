import unittest
from common.requests_handler import RequestsHandler
class LoginTest(unittest.TestCase):
    def setUp(self) :
        #请求类实例化
        self.req=RequestsHandler()
    def tearDown(self):
        self.req.close_session()
    def test_login_success(self):
        login_url='http://dev.api.maltbaby.com.cn/usercenter/sso/v1/bMoblieRegisterLogin'
        payload={
            "mobile": "15088656827",
            "verificationCode": "1234"
        }
        res=self.req.visit('post',login_url,json=payload)
        self.assertEqual('00000000',res['code'])
if __name__=='__main__':
    unittest.main()
