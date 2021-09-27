#response相关属性
import requests

response = requests.get('http://httpbin.org')
print(type(response.status_code),response.status_code)#状态码
print(type(response.headers),response.headers)#响应头
print(type(response.cookies),response.cookies)#cookies
print(type(response.url),response.url)#请求的url
print(type(response.history),response.history)#访问的历史记录