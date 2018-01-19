from numpy import *

import operator
import matplotlib
import matplotlib.pyplot as plt

# 定义一个数据集合，返回值是包含四个训练样本的训练集，以及一个标签类别

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

# 通过inX输入一个数据实例，dataSet为训练集，labels为类别，k表示前k个和输入数据实例距离最小的点的

def classify0(inX,dataSet,labels,k):
	# shape[0]表示取dataSet的行数，shape[1]表示取dataSet的列数
	dataSetSize = dataSet.shape[0]
	# tile表示将inX扩展成dataSetSize行的数组，然后两个相减，得到差值diffMat
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	# sum(axis=1)表示[[1,2],[3,4]]=>[3,7],sum(axis=0)表示[[1,2],[3,4]]=>[4,6]
	sqDistances = sqDiffMat.sum(axis=1)
	# 得到距离
	distances = sqDistances**0.5
	# 排序，得到索引值
	sortedDistIndicies = distances.argsort()
	# 初始化一个空字典，以便后面存储
	classCount = {}

	for i in range(k):
		
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]


def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	# print returnMat
	# print classLabelVector
	return returnMat,classLabelVector

datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
print datingDataMat
# print array(datingLabels)
# print 15.0*array(datingLabels)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()

# import numpy
# from mpl_toolkits.mplot3d import Axes3D
# datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],datingDataMat[:,2],15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
# plt.show()

def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet, ranges, minVals