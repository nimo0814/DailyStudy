# -*- coding:utf-8 -*-
# @Time  :2021/12/27 5:48 下午
# @AUTHOR :nimo
# @File :DES_demo.py
import binascii
from pyDes import des,CBC,PAD_PKCS5
import base64
class DEncry:
    def __init__(self):
        self.Des_Key="12345678"
        self.Des_IV='abcdefgh'
    #使用DES加base64的形式加密
    def des_encrypt(self,s):
        k=des(self.Des_Key,CBC,self.Des_IV,pad=None,padmode=PAD_PKCS5)
        EncryptStr=k.encrypt(s)
        return base64.b64encode(EncryptStr).decode()#转base64编码返回

    def des_descrypt(self,s):
       s=base64.b64decode(s)
       k=des(self.Des_Key,CBC,self.Des_IV,pad=None,padmode=PAD_PKCS5)
       DecryptStr=k.decrypt(s,padmode=PAD_PKCS5)
       return DecryptStr.decode()

if __name__=="__main__":
    de=DEncry()
    passwd=de.des_encrypt("9999999")
    print("passwd:%s" %passwd)
    ret=de.des_descrypt(passwd)
    print("result:%s" %ret)
