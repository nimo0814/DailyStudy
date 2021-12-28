# -*- coding:utf-8 -*-
# @Time  :2021/12/28 9:46 上午
# @AUTHOR :nimo
# @File :AES_demo.py
import base64
import binascii
from Crypto.Cipher import AES

class Aescrypt():
    def __init__(self,key,model,iv):
        self.key=self.add_16(key)
        self.model=model
        self.iv=self.add_16(iv)

    def add_16(self,par):
        if type(par)==str:
            par=par.encode()
        while len(par)%16!=0:
            par+=b'\x00'
        return par

    def aesencrypt(self,text):
        text=self.add_16(text)
        if self.model==AES.MODE_CBC:
            self.aes=AES.new(self.key,self.model,self.iv)
        elif self.model==AES.MODE_ECB:
            self.aes=AES.new(self.key,self.model)
        self.encrypt_text=self.aes.encrypt(text)
        return self.encrypt_text

    def aesdecrypt(self,text):
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key, self.model, self.iv)
        elif self.model == AES.MODE_ECB:
            self.aes = AES.new(self.key, self.model)
        self.decrypt_text = self.aes.decrypt(text)
        self.decrypt_text = self.decrypt_text.strip(b"\x00")
        return self.decrypt_text

if __name__ =='__main__':
    password="12345"
    iv='1233455666'

    aescryptor=Aescrypt(password,AES.MODE_CBC,iv)
    #aescryptor=Aescrypt(password,AES.MODE_ECB)
    text="软件测试学习"
    # text='wdddfffffff'
    en_text=aescryptor.aesencrypt(text)
    print(en_text)
    print("密文：",(base64.b64encode(en_text)))
    text=aescryptor.aesdecrypt(en_text)
    print("明文：",text.decode())