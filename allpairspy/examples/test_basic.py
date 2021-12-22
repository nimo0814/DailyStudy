# -*- coding:utf-8 -*-
# @Time  :2021/12/22 7:50 下午
# @AUTHOR :nimo
# @File :test_basic.py
from allpairspy import AllPairs

parameters = [
    ["Brand X", "Brand Y"],
    ["98", "NT", "2000", "XP"],
    ["Internal", "Modem"],
    ["Salaried", "Hourly", "Part-Time", "Contr."],
    [6, 10, 15, 30, 60],
]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))