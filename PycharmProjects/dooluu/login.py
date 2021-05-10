from selenium import webdriver
import  webbrowser as web
import os
import datetime,time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

def login():
    driver.get("http://dev.mp.dooluu.com.cn/login")
    #driver.maximize_window()
    time.sleep(5)
    if driver.find_element_by_class_name('qrcode active'):
        print('get the QRCodeImgUrl.....')
        print(driver.find_element_by_class_name('qrcode active').find_element_by_tag_name('img').get_attribute('src'))
        driver.get(
            driver.find_element_by_class_name('qrcode active').find_element_by_tag_name('img').get_attribute('src'))
"""
    while True:
        try:
            if driver.find_element_by_link_text("手机扫描 安全登录"):
                print("请扫码登录...")
                time.sleep(1)

        except NoSuchElementException:
            print("成功登录...")
            print(driver.current_url)
            break

    time.sleep(1)
"""
login()