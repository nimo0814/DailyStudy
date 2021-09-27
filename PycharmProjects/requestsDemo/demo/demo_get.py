#get请求
import requests

response = requests.get('https://www.dedao.cn/')
print(response.text)