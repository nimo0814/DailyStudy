#post请求
import requests

data = {
    'name':'Thanlon',
    'age':22,
    'sex':'男'

}
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)