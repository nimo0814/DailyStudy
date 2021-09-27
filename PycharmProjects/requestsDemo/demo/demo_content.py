#获取二进制数据
import requests

response = requests.get('https://www.baidu.com/img/dong_5af13a1a6fd9fb2c587e68ca5038a3c8.gif')
print(type(response.text))
print(type(response.content))
#print(response.text)
#print(response.content)#二进制流