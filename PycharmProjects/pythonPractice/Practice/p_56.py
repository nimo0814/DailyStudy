"""
题目：画图，学用circle画圆形。　
"""
import numpy as np#导入数据包主要处理数据
import matplotlib.pyplot as plt#导入图形包
x=y=np.arange(-4,4,0.1)#函数返回一个有终点和起点的固定步长的排列
x,y=np.meshgrid(x,y)#生成网格点坐标矩阵
plt.contour(x,y,x**2+y**2,[9])#x**2 + y**2 = 9 的圆形

plt.axis('scaled')
plt.show()