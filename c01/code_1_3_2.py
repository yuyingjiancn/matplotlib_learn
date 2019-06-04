# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False      # 解决保存图像是负号'-'显示为方块的问题

# 在0.5到3.5之间均匀的取100个数
x = np.linspace(0.05, 10, 1000)

#计算x的sin值
y = np.random.rand(1000)

'''
c: 散点图标记颜色
label: 系列名称
'''
plt.scatter(x, y, c='r', marker='s', label='散点图')
plt.legend()  # 显示系列
plt.show()