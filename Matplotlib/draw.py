# -*-coding:utf-8-*-
# 完美解决中文绘图乱码：
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False  

# ==============================
import matplotlib.pyplot as plt
import numpy as np
# ==============================

# 将0-10等分成50份，将值赋值给x
x = np.linspace(-10,10,351)


y1 = 0.5 * x + 2
y2 = 4*x ** 2
# 弹出窗口名为：figure3，大小10:5
plt.figure(num=3,figsize=(10,5))

# 实现图例,方式1:
l1, = plt.plot(x,y1,label='实线')
l2, = plt.plot(x,y2,color='red',linewidth=3,linestyle='--',label='虚线')
plt.legend(loc='upper left')

# 实现图例方式2:
# l1, = plt.plot(x, y1)
# l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
# plt.legend(handles=[l1, l2], labels=['实线', '虚线'],  loc=1)



# 设置x、y轴的坐标范围：(注意下面的代码会对次有影响，想查看效果，应将下方的注释掉)
plt.xlim(0,10)
plt.ylim(3,5)



# 设置轴的名称：
plt.xlabel('X轴')
plt.ylabel('Y轴')



# 设置轴上的名字：

# 将-10到10分成20份，new_ticks得到每个的值
new_ticks = np.linspace(-10,10,21)
# 实现坐标轴的按数值划分：
plt.xticks(new_ticks)
# 实现坐标轴的按特定字符划分：
plt.yticks([-2,-1, 0, 1, 2],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])



# 设置坐标轴的位置,可以保证两轴交点为原点
# 获得轴
ax = plt.gca()
# 设置轴可见情况：
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('green')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 以x轴为界，上下移动轴：
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(('data', 0))
# 以y轴为界，左右移动：
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
