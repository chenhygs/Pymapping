# -*- coding: utf-8 -*-
"""
Created on C Apr 30 11:37:15 2022

@author: Administrator
"""

# 导入库
import matplotlib.pyplot as plt
plt.subplot(2,1,1)
# 设置数据
day = [1,2,3,4,5,6,7]
my_body_weight = [75,75.1,74.9,74,73.9,73,70]
other_body_weight = [56.3,56,55.9,54,53.9,53,50]

# 堆积柱状图
plt.bar(day,my_body_weight,
       color = "r",
       label = "my body weight")
plt.bar(day,other_body_weight,
       color = "b",
       # 将上述数据置于底层
       bottom = my_body_weight,
       label = "other body weight")
plt.xlabel("Day")
plt.ylabel("Weight (kg)")
plt.ylim(0,160)
# 设置间距
plt.yticks([0,40,80,120,160])
plt.legend()

plt.subplot(2,1,2)
#条形堆积图
plt.barh(day,my_body_weight,
       color = "r",
       label = "my body weight")
plt.barh(day,other_body_weight,
       color = "b",
       # 将上述数据置于底层
       left= my_body_weight,
       label = "other body weight")
plt.ylabel("Day")
plt.xlim(0,160)
plt.xlabel("Weight (kg)")
# 使用loc确定legend的位置
# 其余的参数还有：
# (‘best’, ‘upper right’, ‘upper left’,
# ‘lower left’, ‘lower right’,
# ‘right’, ‘center left’, ‘center ,
# right’, ‘lower center’,
# ‘upper center’, ‘center’)
plt.legend(loc = "lower left")
