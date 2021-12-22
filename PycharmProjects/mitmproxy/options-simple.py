# -*- coding:utf-8 -*-
# @Time  :2021/12/22 2:19 下午
# @AUTHOR :nimo
# @File :options-simple.py
from mitmproxy import ctx

class AddHeader:
    def __init__(self):
        self.num=0

    def load(self,loader):
        loader.add_option(
            name="addheader",
            typespec=bool,
            default=False,
            help="Add a count header to responses",

        )

    def response(self,flow):
        if ctx.options.addheader:
            self.num=self.num+1
            flow.response.headers["count"]=str(self.num)

addons=[
    AddHeader()
]
