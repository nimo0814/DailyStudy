#保存二进制文件（图片、视频）
import requests

response = requests.get('https://www.baidu.com/img/dong_5af13a1a6fd9fb2c587e68ca5038a3c8.gif')
with open('image.gif','wb') as f:
    f.write(response.content)
    f.close()