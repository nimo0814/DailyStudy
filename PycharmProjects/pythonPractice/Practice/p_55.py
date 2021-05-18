"""
题目：学习使用按位取反~。

说明：

二进制数在内存中以补码的形式存储。

按位取反：二进制每一位取反，0 变 1，1 变 0。

最高位为符号位，正数的符号位为 0，负数为 1。

对正数来说，最高位为 0，其余各位代表数值本身(以二进制表示)，如 +42 的补码为 00101010。

对负数而言，把该数绝对值的补码按位取反，然后对整个数加 1，即得该数的补码。如 -42 的补码为 11010110(00101010 按位取反
11010101+1 即 11010110)。
"""
a=7
b=~a

c=-7
d=~c

print('变量a 取反结果为：%d' %b)
print('变量c 取反结果为：%d' %d)

"""
说明：

～7，对 7 进行取反，7 的补码是 00000111 对补码取反得到 11111000，最高位 1 为符号位，表示负数，所以该补码对应的整数为 -8。

~-7 对 -7 进行取反，-7 的补码是 11111001 对补码取反得到 00000110，最高位 0 为符号位，表示正数，所以补码对应的整数为 6。
"""