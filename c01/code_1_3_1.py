import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False      # 解决保存图像是负号'-'显示为方块的问题

# 在0.5到3.5之间均匀的取100个数
x = np.linspace(0.05, 10, 1000)

#计算x的sin值
y = np.cos(x)

'''
linestyle或者ls: 线的样式 see docs of Line2D.set_linestyle for valid values
                '-', '--', '-.', ':'       
linewidth或者lw: 线的宽度
label: 系列名称
'''
plt.plot(x, y, linestyle='-.', linewidth='2', label='余弦函数')
plt.legend()  # 显示系列
plt.show()