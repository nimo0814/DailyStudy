"""
题目：画图，学用line画直线。
"""
import matplotlib.pyplot as plt
import  numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linestyle='dotted')
plt.show()