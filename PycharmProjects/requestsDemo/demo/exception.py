#异常处理
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException,ConnectionError

try:
    response=requests.get('http://httpbin.org', timeout=0.3)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http Error')
except RequestException:
    print('Request Error')