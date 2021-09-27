#解析json
import requests,json

response=requests.get('http://www.httpbin.org/get')
print(type(response.text))#返回相应text的类型
print(response.json())#返回响应的json
print(type(response.json()))#打印出响应json的类型为字典