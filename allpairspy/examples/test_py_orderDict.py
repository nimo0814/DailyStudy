# -*- coding:utf-8 -*-
# @Time  :2021/12/22 8:06 下午
# @AUTHOR :nimo
# @File :test_py_orderDict.py
from collections import OrderedDict

import pytest
from allpairspy import AllPairs

def function_to_be_tested(brand, operating_system, minute) -> bool:
    # do something
    return True

class TestParameterized(object):
    @pytest.mark.parametrize(
        ["pair"],
        [
            [pair]
            for pair in AllPairs(
                OrderedDict(
                    {
                        "brand": ["Brand X", "Brand Y"],
                        "operating_system": ["98", "NT", "2000", "XP"],
                        "minute": [10, 15, 30, 60],
                    }
                )
            )
        ],
    )
    def test(self, pair):
        assert function_to_be_tested(pair.brand, pair.operating_system, pair.minute)