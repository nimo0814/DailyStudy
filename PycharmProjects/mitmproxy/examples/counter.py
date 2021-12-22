# -*- coding:utf-8 -*-
# @Time  :2021/12/22 6:21 下午
# @AUTHOR :nimo
# @File :counter.py
from mitmproxy import ctx
class Counter:
    def __init__(self):
        self.num=0

    def request(self,flow):
        self.num=self.num+1
        ctx.log.info("We've seen %d flows" %self.num)