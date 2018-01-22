# -*-coding:utf-8-*-
from math import log


dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
'''
一、计算香农熵步骤：

设总共有n种类别

1.计算某第i类别所占全部类别数的比例（概率）： p(i)；

2.计算信息-log2(p(i));

3.求熵：即求n种类别的信息的期望。

'''
# My method
# 貌似不够健壮：
def calcShannonEnt(dataSet):
	numAll = len(dataSet)
	countY = 0
	countN = 0
	for featVec in dataSet:
		if featVec[-1] == 'yes':
			countY += 1
		else:
			countN += 1
	pY = float(countY)/numAll
	pN = float(countN)/numAll
	infoY = -log(pY,2)
	infoN = -log(pN,2)
	shannonEnt = pY*infoY + pN*infoN
	return shannonEnt
print calcShannonEnt(dataSet)

'''
二、划分数据集

1.这里相当于是对树的根节点进行分叉，即对数据集dataSet按照某特征值进行划分；

2.分叉完事后，要得到新的小的数据集，同时数据集的特征减少1，并完成了一次划分；

3.注意参照图3-2理解。

4.编码需要实现：如果dataSet上的axis轴上的值等于value，那么取出该行的其它特征值存到数组

'''
def splitDataSet(dataSet,axis,value):
	numAll = len(dataSet)
	retDataSet = []
	for i in range(numAll):
		if dataSet[i][axis] == value:
			'''
			front = dataSet[i][:axis+1]
			print front
			rear = dataSet[i][axis+1:]
			print rear
			注意：这种做法是错误的，这里的extend返回值是None，改变的仅仅是front的值，
			并不会将修改后的值赋值到reduceFR。部分函数是返回None，有些则是可以返回到
			赋值的变量的，特此提醒！
			reduceFR = front.extend(rear)
			print reduceFR
			retDataSet.append(reduceFR)
			'''
			reduceFR = dataSet[i][:axis]
			rear = dataSet[i][axis+1:]
			reduceFR.extend(rear)
			retDataSet.append(reduceFR)		
	return retDataSet

print splitDataSet(dataSet,0,1)
