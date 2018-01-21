# -*-coding:utf-8-*-
from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelsCounts = {}
	for featVec in dataSet:
		# print featVec
		currentLabel = featVec[-1]
		print currentLabel
		if currentLabel not in labelsCounts.keys():
			labelsCounts[currentLabel] = 1
		else:
			labelsCounts[currentLabel] +=1
		# print labelsCounts
		# labelsCounts[currentLabel] += 1
		print labelsCounts
	shannoEnt = 0.0
	for key in labelsCounts:
		print key
		prob = float(labelsCounts[key])/numEntries
		shannoEnt -= prob * log(prob,2)
	return shannoEnt

def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels

# 这个函数的功能是：讲第axis列的值和value比较，相同，则拿到除了axis列的数组，追加到retDataSet数组中
def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		# print featVec
		# print featVec[:2]
		# 从这可以看出axis指的是域（列）
		if featVec[axis] == value:
			# 这里是截取字符串，axis=0表示，0到0，为空。axis=1，表示0到1，截取数组里的第一个字符。
			# 截取axis前面所有
			reduceFeatVec = featVec[:axis]
			# print reduceFeatVec
			# 这行的主要目的是除去axis域那一列的值，只计算其他两列
			# 截取axis后面所有，并和上面截取的合并
			reduceFeatVec.extend(featVec[axis+1:])
			# print reduceFeatVec
			# 追加到数组retDataSet中
			retDataSet.append(reduceFeatVec)
	return retDataSet

myDat,labels = createDataSet()

# print myDat
# print calcShannonEnt(myDat)

print splitDataSet(myDat,1,1)