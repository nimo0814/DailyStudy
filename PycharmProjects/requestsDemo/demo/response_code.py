#状态码判断
import requests
response = requests.get('http://httpbin.org')
if not response.status_code == requests.codes.ok:
    pass
else:
    print('Request Successfully')