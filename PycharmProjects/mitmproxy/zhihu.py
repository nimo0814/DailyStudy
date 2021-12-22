# -*- coding:utf-8 -*-
# @Time  :2021/12/22 4:28 下午
# @AUTHOR :nimo
# @File :zhihu.py
import json
import re
from mitmproxy import ctx
from mitmproxy import http
class zhihu:

    def response(self,flow:http.HTTPFlow):
        # 提取请求的url地址
        request_url=flow.request.url

        if bool(re.search(r"zhihu",request_url)):
            print("request_url>>>",request_url)
            response_body=flow.response.text
            print("response_body>>>",response_body)
            response_url=flow.request.url
            print("response_url>>>",response_url)
            ctx.log.info("打印输出："+response_body)
            data=json.loads(response_body)
            try:
                ware_infos=data.get(data)
                av_info={}
                if ware_infos is not None:
                    for ware_info in ware_infos:
                        av_info["标题"]=ware_info['card']['title']['plain_text']
                        av_info["视频地址"]=ware_info['card']['action']['intent_url']
                        av_info["UP主"] = ware_info['card']['author']['name']
                        print(av_info)
            except:
                ctx.log.info("跳过")
addons=[
    zhihu()
]

