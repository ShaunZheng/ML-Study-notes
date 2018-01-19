#-*-coding:utf-8-*- 
from numpy import *
import operator
# 定义一个数据集合，返回值是包含四个训练样本的训练集，以及一个标签类别
def createDataSet():
	group = array([[1.0,1.1],[0,0],[1.0,1.0],[0,0.1]])
	labels = ['A','B','A','B']
	return group,labels
group,labels =  createDataSet()
print group
print type(group)
# 通过inX输入一个数据实例，dataSet为训练集，labels为类别，k表示前k个和输入数据实例距离最小的点的

def classify0(inX,dataSet,labels,k):
	# shape[0]表示取dataSet的行数，shape[1]表示取dataSet的列数
	dataSetSize = dataSet.shape[0]
	print dataSetSize
	# tile表示将inX扩展成dataSetSize行的数组，然后两个相减，得到差值diffMat
	print tile(inX,(dataSetSize,1))
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	print diffMat
	sqDiffMat = diffMat**2
	print sqDiffMat
	# sum(axis=1)表示[[1,2],[3,4]]=>[3,7],sum(axis=0)表示[[1,2],[3,4]]=>[4,6]
	sqDistances = sqDiffMat.sum(axis=1)
	print sqDistances
	# 得到距离
	distances = sqDistances**0.5
	print distances
	# 排序，得到索引值
	sortedDistIndicies = distances.argsort()
	print sortedDistIndicies
	print type(sortedDistIndicies)
	# 初始化一个空字典，以便后面存储
	classCount = {}

	for i in range(k):
		
		voteIlabel = labels[sortedDistIndicies[i]]
		print voteIlabel

		print classCount.get(voteIlabel,0)
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
		print classCount
	
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	print sortedClassCount

	return sortedClassCount[0][0]

print classify0([1,1],group,labels,3)