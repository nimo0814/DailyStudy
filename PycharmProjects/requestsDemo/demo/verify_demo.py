#证书验证
import requests,urllib3

urllib3.disable_warnings()#消除警报信息
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)#没有进行证书验证，有警报信息