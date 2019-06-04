import numpy as np
import matplotlib.pyplot as plt

#在0.5到3.5之间均匀的取100个数
x = np.linspace(0.5, 3.5, 100)

#计算x的sin值
y = np.sin(x)

#在标准正态分布中随机地取100个数
y1 = np.random.randn(100)