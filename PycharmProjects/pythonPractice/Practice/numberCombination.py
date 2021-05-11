"""
实例001：数字组合
题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    """
    permutations(iterable [,r]):创建一个迭代器，返回iterable中所有长度为r的项目序列，
    如果省略了r，那么序列的长度与iterable中的项目数量相同
    """
    print(i)
    sum2+=1
print(sum2)