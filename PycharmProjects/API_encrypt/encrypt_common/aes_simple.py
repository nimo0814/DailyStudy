# -*- coding:utf-8 -*-
# @Time  :2021/12/28 10:14 上午
# @AUTHOR :nimo
# @File :aes_simple.py
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
BLOCK_SIZE=32

password='1234567890123456'#秘钥
text='1234567890123456'#需要加密的内容
model=AES.MODE_ECB#定义模式
aes=AES.new(password.encode('utf8'),model)#创建一个aes对象

en_text=aes.encrypt(pad(text.encode('utf8'),BLOCK_SIZE))#加密明文
print(en_text)
en_text=base64.encodebytes(en_text)#返回的字节型数据进行base64编码
print(en_text)
en_text=en_text.decode('utf8')#将字节型数据转换成python中的字符串类型
print(en_text.strip())
