# -*-coding:utf-8-*-
from math import log
# 计算给定数据集的香农熵
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelsCounts = {}
	for featVec in dataSet:
		# print featVec
		currentLabel = featVec[-1]
		# print currentLabel
		if currentLabel not in labelsCounts.keys():
			labelsCounts[currentLabel] = 1
		else:
			labelsCounts[currentLabel] +=1
		# print labelsCounts
		# labelsCounts[currentLabel] += 1
		# print labelsCounts
	shannoEnt = 0.0
	for key in labelsCounts:
		# print key
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
# 选择最好的最好的划分特征
def chooseBestFeatureToSplit(dataSet):
	# 
	numFeatures = len(dataSet[0]) - 1
	# 计算给定数据集的香农熵
	baseEntryopy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		# 列表生成式：得到每个example的第i列的值，得到一个数组
		featList = [example[i] for example in dataSet]
		print featList
		# set()方法，将重复值合并，如12123->123
		uniqueVals = set(featList)
		# print uniqueVals
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		# print newEntropy
		# 信息增益
		infoGain = baseEntryopy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	print newEntropy
	return bestFeature
		

myDat,labels = createDataSet()

print 'myDat=>',myDat
print 'myDat[0]=>', len(myDat[0])
# print calcShannonEnt(myDat)

print 'splitDataSet(myDat,1,1)=>',splitDataSet(myDat,1,1)

test0 = chooseBestFeatureToSplit(myDat)
print '最好的划分特征是：',test0

# for i in xrange(3):
# 	x = [example[i] for example in myDat]
# 	print x

# 得到出现次数最多的分类名称
def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys:
			classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),key = operator.iteritems(1),reverse = True)
	return sortedClassCount