# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
# 在指定的间隔内返回均匀间隔的数字，0-3pi,之间取100个点，并赋给x
x = np.linspace(0, 3 * np.pi, 100)

# 把x放入sin求得y
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 表示把显示界面分割成1*2的网格。其中，第一个参数是行数，第二个参数是列数，第三个参数表示图形的标号。
plt.subplot(1,2,1)
# 第一个图的标题为：f(x)=sin(x)
plt.title(r'$f(x)=sin(x)$')
# x为x轴数据, y为y轴数据
plt.plot(x, y)


x1 = [t*0.375*np.pi for t in x]  # x1 = x*0.375*np.pi
y1 = np.sin(x1)                  # 将x1放入sin函数求y1

# 表示把显示界面分割成1*2的网格,第2个图形。
plt.subplot(1,2,2)

# 第二个图的标题为f(x)=sin(\omega x)，\omega = \frac{3}{8} \pi
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')
plt.plot(x, y1)  # x为x轴数据, y1为y轴数据
plt.show()  # 显示图片