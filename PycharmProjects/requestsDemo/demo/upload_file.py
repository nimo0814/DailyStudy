#文件上传
import requests
files ={
    'file':open('image.gif','rb')
}
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)