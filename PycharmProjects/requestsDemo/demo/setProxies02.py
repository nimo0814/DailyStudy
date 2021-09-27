#代理的设置（存在用户名和密码的情况下）
import requests

proxies={
    'http': 'http://user:password@127.0.0.1:9743',
    'https': 'https://user:password@127.0.0.1:9743'
}
response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)