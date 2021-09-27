#会话维持：模拟登陆（相当于一个浏览器请求）
import requests

s=requests.Session()
s.get('http://httpbin.org/cookies/set/BDORZ/123456')
response = s.get('http://httpbin.org/cookies')
print(response.text)