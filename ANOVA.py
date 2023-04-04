# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:12:06 2022

@author: Administrator
"""
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#读取数据
data=pd.read_excel("E:\luan论文\品质整理.xlsx")
df=pd.DataFrame(data)
print(df.head(5))
print(df.describe())

a=0.01
for i in range(5,23):
       factor=df.iloc[:,i]
       formula='factor~主区+裂区+主区*裂区'
       anova_results = anova_lm(ols(formula,df).fit())
       print(anova_results)
       print(pairwise_tukeyhsd(factor,df['主区'],alpha=a))
       print(pairwise_tukeyhsd(factor,df['裂区'],alpha=a))
       i=i+1
