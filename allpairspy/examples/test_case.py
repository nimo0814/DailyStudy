# -*- coding:utf-8 -*-
# @Time  :2021/12/22 7:36 下午
# @AUTHOR :nimo
# @File :test_case.py
import pytest
from allpairspy import AllPairs

def function_to_be_tested( sex, grade, age):
    if grade == "一年级" and age == "10-13岁":
        return False
    return True

class TestParameterized(object):

    @pytest.mark.parametrize(["sex", "grade", "age"], [
        value_list for value_list in AllPairs([
            [u"男", u"女"],
            ["一年级", "二年级", "三年级", "四年级", "五年级"],
            ["8岁以下", "8-10岁", "10-13岁"]
        ])
    ])
    def test(self, sex, grade, age):
        assert function_to_be_tested(sex, grade, age)