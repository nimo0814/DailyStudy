from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    driver=webdriver.Chrome()
    host='127.0.0.1:4444'
    dc={'browseName':'chrome'}
    driver=Remote(command_executor='http://'+host+'/wd/hub',desired_capabilities=dc)
    return driver
if __name__=='__main__':
    dr=browser()
    dr.get("http://www.baidu.com")
    dr.quit()