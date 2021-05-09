from selenium import webdriver
import os


#截图函数
def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))#获取文件所在目录的完整路径
    base_dir=str(base_dir)#将地址转为字符串
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/test_case')[0]#以/test_case为分隔符，取第一个分割的部分
    file_path=base+"/report/image/"+file_name
    driver.get_screenshot_as_file(file_path)#保存截图

if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver,'baidu.jpg')
    driver.quit()