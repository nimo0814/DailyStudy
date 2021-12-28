# -*- coding:utf-8 -*-
# @Time  :2021/12/28 3:00 下午
# @AUTHOR :nimo
# @File :test_api.py
import base64
import json

from Crypto.Cipher import AES
"""AES加密算法"""
BLOCK_SIZE=16
unpad=lambda s:s[0:-ord(s[-1])]

def decrypyBase64(src):
    return base64.urlsafe_b64decode(src)

def decryptAES(src):
    """解析AES密文"""
    src=decrypyBase64(src)
    key = b'W7v4D60fds2Cmk2U'
    iv = b"1172311105789011"
    cryptor=AES.new(key,AES.MODE_CBC,iv)
    text=cryptor.decrypt(src).decode()
    return unpad(text)

def aes_encryption(request):
    if request.method=='POST':
        data=request.POST.get("data","")
    else:
        return "error"
    if data=="":
        return "data null"
    #解密
    decode=decryptAES(data)
    #转换为字典
    dict_data=json.loads(decode)
    return dict_data


class JsonResponse:
    pass


class ObjectDoesNotExist:
    pass


class Guest:
    pass


def get_guest_list(request):
    dict_data=aes_encryption(request)
    if dict_data=="data null":
        return JsonResponse({'status':10010,'message':'data null'})
    if dict_data=="error":
        return JsonResponse({'status':10011,'message':'request error'})
    #取出对应的发布会id和手机号
    try:
        eid=dict_data['eid']
        phone=dict_data['phone']
    except KeyError:
        return JsonResponse({'status':10012,'message':'parameter error'})
    if eid=='':
        return JsonResponse({'status':10021,'message':'eid cannot be empty'})
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})
