#超时设置
import requests
response = requests.get('http://httpbin.org',timeout=1)
print(response.status_code)