# -*- coding:utf-8 -*-
# @Time  :2021/12/28 10:53 上午
# @AUTHOR :nimo
# @File :aes_simple2.py
import base64
from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad,unpad
# BLOCK_SIZE=32
def add_to_16(par):
    par=par.encode()#先将字符串类型数据转换成字节型数据
    while len(par)%16!=0:#对字节型数据进行长度判断
        par+=b'\x00'#如果字节型数据长度不是16倍整数就进行补充
    return par

password='123456'#秘钥
text='123'#需要加密的内容
model=AES.MODE_ECB#定义模式
aes=AES.new(add_to_16(password),model)#创建一个aes对象

en_text=aes.encrypt(add_to_16(text))#加密明文
print(en_text)
en_text=base64.encodebytes(en_text)#返回的字节型数据进行base64编码
print(en_text)
en_text=en_text.decode('utf8')#将字节型数据转换成python中的字符串类型
print(en_text.strip())
