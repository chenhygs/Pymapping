# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a chy script file.
"""
import numpy as np
import matplotlib.pyplot as plt  # 导入所需的库

x, y = np.meshgrid(np.linspace(0, 20, 20), np.linspace(0, 20, 20))  # 定义网格

u = x**(-3)+x*y**2
v = y**3*np.sin(13/60)  # 定义向量

plt.quiver(x, y, u, v)  # 绘场图


def f(x, y):
    return(x**(-3)-x*y**2+y**3*np.sin(13/60))  # 定义函数


plt.contour(x, y, f(x, y))
contour = plt.contour(x, y, f(x, y))
plt.clabel(contour, colors='k')  # 绘制等值线图
plt.show()