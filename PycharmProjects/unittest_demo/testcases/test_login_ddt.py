import unittest
from common.requests_handler import RequestsHandler
from common.excel_handler import ExcelHandler
import ddt
import json
@ddt.ddt
class TestLogin(unittest.TestCase):
    #读取Excel中的数据
    excel=ExcelHandler('../data/test_cases.xlsx')
    case_data=excel.read_excel('login')
    print(case_data)
    def setUp(self):
        #请求类实例化
        self.req=RequestsHandler()
    def tearDown(self):
        self.req.close_session()
    @ddt.data(*case_data)
    def test_login_success(self,items):
        #请求接口
        res=self.req.visit(method=items['method'],url=items['url'],json=json.loads(items['payloads']))
        try:
            #断言
            self.assertEqual(res['code'],items['expected_result'])
            result='Pass'
        except AssertionError as e:
            result='Fail'
            raise e
        finally:
           #将响应的状态码写到excel的第9列，即写入返回的状态码
           TestLogin.excel.write_excel("../data/test_cases.xlsx",'login',items['case_id']+1,9,res['code'])
           #如果断言成功，则在第10行（测试结果）写入Pass，否则写入Fail
           TestLogin.excel.write_excel("../data/test_cases.xlsx",'login',items['case_id']+1,10,result)
if __name__=='__main__':
    unittest.main()
