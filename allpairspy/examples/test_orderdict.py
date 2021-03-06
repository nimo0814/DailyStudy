# -*- coding:utf-8 -*-
# @Time  :2021/12/22 7:58 下午
# @AUTHOR :nimo
# @File :test_orderdict.py
from collections import OrderedDict
from allpairspy import AllPairs

parameters = OrderedDict({
    "brand": ["Brand X", "Brand Y"],
    "os": ["98", "NT", "2000", "XP"],
    "minute": [15, 30, 60],
})

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))