import time
from logging import root

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://dev.bos.maltbaby.com.cn/login")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[1]/div/div/span/span/input').clear()
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[1]/div/div/span/span/input').send_keys('nimo')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/div/div/span/span/input').clear()
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/div/div/span/span/input').send_keys('Enjoy*0726')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[3]/div/div/span/button').click()
