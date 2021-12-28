# -*- coding:utf-8 -*-
# @Time  :2021/12/22 1:58 下午
# @AUTHOR :nimo
# @File :anatomy.py
from mitmproxy import ctx
class Counter:
    def __init__(self):
        self.num=0

    def request(self,flow):
        self.num=self.num+1
        ctx.log.info("We've seen %d flows" %self.num)

addons=[
    Counter()
]