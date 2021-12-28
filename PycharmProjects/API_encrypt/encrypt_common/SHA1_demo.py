# -*- coding:utf-8 -*-
# @Time  :2021/12/27 3:54 下午
# @AUTHOR :nimo
# @File :SHA1_demo.py
import hashlib
#创建sha1对象
sha1=hashlib.sha1()
data='hello world'
sha1.update(data.encode(encoding='utf-8'))
sha1_data=sha1.hexdigest()
print("SHA1加密前："+data)
print("SHA1加密后："+sha1_data)