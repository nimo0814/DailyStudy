#post请求，添加headers
import requests

data={
'name': 'Thanlon',
    'age': 22,
    'sex': '男'
}
headers={
'user-agent': 'Mouser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'

}
response=requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.text)