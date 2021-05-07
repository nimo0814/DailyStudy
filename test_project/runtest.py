import unittest,time
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import  smtplib
import os

#定义发送邮件
def semd_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告：",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login("useranem@126.com","123456")
    smtp.sendmail(("useranem@126.com", "receiver@126.com", msg.as_string()))
    smtp.quit()
    print("email has send out")

#查找测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

#定义测试用例的目录
test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    filename=test_dir+'/'+now+'result.html'
    fp=open(filename,'w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况:')
    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_mail(new_report)
