# -*- coding:utf-8 -*-
# @Time  :2021/12/22 8:01 下午
# @AUTHOR :nimo
# @File :test_pytest.py
import pytest
from allpairspy import AllPairs

def function_to_be_tested(brand, operating_system, minute) -> bool:
    # do something
    return True

class TestParameterized(object):
    @pytest.mark.parametrize(["brand", "operating_system", "minute"], [
        values for values in AllPairs([
            ["Brand X", "Brand Y"],
            ["98", "NT", "2000", "XP"],
            [10, 15, 30, 60]
        ])
    ])
    def test(self, brand, operating_system, minute):
        assert function_to_be_tested(brand, operating_system, minute)