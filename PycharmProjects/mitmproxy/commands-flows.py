# -*- coding:utf-8 -*-
# @Time  :2021/12/22 3:52 下午
# @AUTHOR :nimo
# @File :commands-flows.py
import typing

from mitmproxy import command
from mitmproxy import ctx
from mitmproxy import flow

class MyAddon:
    @command.command("myaddon.addheader")
    def addheader(self,flows:typing.Sequence[flow.Flow])->None:
        for f in flows:
            f.request.headers["myheader"]="value"
        ctx.log.alert("done")


addons=[
    MyAddon()
]
