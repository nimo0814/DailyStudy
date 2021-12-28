# -*- coding:utf-8 -*-
# @Time  :2021/12/27 4:06 下午
# @AUTHOR :nimo
# @File :HMAC_demo.py
import hmac
import hashlib
#第一个参数是密钥key，第二个参数是待加密的字符串，第三个参数是hash函数
#key=bytes('key',encoding='utf-8')
key=b'key'
str1='Hello,'
str2='World!'
str=str1+str2
h1=hmac.new(key,str1.encode('utf-8'))
#字节缓冲区
h1.update(str2.encode('utf-8'))
#十六进制hash字符串
ret1=h1.hexdigest()
print(str)
print(type(ret1),len(ret1),ret1)

h2=hmac.new(key,str.encode('utf-8'),digestmod=hashlib.md5)
h2.update(str.encode('utf-8'))
ret2=h2.hexdigest()
print(type(ret2),len(ret2),ret2)

