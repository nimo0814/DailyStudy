# -*- coding:utf-8 -*-
# @Time  :2021/12/27 3:07 下午
# @AUTHOR :nimo
# @File :md5_demo.py
import hashlib
#待加密信息
str='this is a MD5 Test.'
#创建MD5对象
m=hashlib.md5()
# Tips
# 此处必须声明encode
# 若写法为m.update(str) 报错为： Unicode-objects must be encoded before hashing
m.update(str.encode(encoding='utf-8'))
print('MD5加密前为：'+str)
print('MD5加密后为：'+m.hexdigest())