# -*-coding:utf-8-*-
from numpy import *
from os import listdir
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

# datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
# print datingDataMat
# print array(datingLabels)
# print 15.0*array(datingLabels)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()

# 3d图绘制
# import numpy
# from mpl_toolkits.mplot3d import Axes3D
# datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],datingDataMat[:,2],15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
# plt.show()

# 对特征值进行归一化
def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet, ranges, minVals

def datingClassTest():
	hoRatio = 0.050
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],6)
		print "分类结果：%d,真实值：%d" % (classifierResult,datingLabels[i])
		if (classifierResult != datingLabels[i]): errorCount +=1.0
	print "错误率 :%f" % (errorCount/float(numTestVecs))
	print "错误个数：%d" % errorCount

# datingClassTest()

def classifyPerson():
	resultList = ['一点也不喜欢','有点喜欢','相当喜欢']
	percentTags = float(raw_input('玩游戏的时间百分比?'))
	ffMiles = float(raw_input('每年的飞行里程？'))
	iceCream = float(raw_input('每年干掉的冰淇淋（升）？'))
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTags,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print '你可能对此人的喜欢程度为：',resultList[classifierResult - 1]

# classifyPerson()

def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		# 注意readline和readlines的区别，前者直接读出，后者有换行符号等.q前者只读一行，后者一次性读完所有行。
		lineStr = fr.readline()
		for j in range(32):
			# 这里就很精妙，i控制行数，j控制列元素，得到一个1024长的array
			returnVect[0,32*i+j] = int(lineStr[j])
	# print lineStr
	return returnVect
# print type(img2vector('testDigits/0_13.txt'))
# print img2vector('testDigits/0_13.txt')[0,0:31]

def handwritingClassTest():
	hwLabels = []
	# trainingDigits为当目录下的一个文件夹，此处遍历该文件夹下的所有的文件名
	trainingFileList = listdir('trainingDigits')
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		# 通过‘.’号，对文件名进行分割，通过[0],实现只取list中的第一个，也就是把.txt给剔除了
		fileStr = fileNameStr.split('.')[0]
		# 同理，取得文件名如0_132的前面的数字0
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)

	testFileList = listdir('testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print '分类结果：%d,真实值：%d' %(classifierResult,classNumStr)
		if (classifierResult != classNumStr):
			errorCount += 1.0
	print '总的分类错误数为：%d' % errorCount
	print '分类错误率为：%f' % (errorCount/float(mTest))
		# print hwLabels
		# print fileStr
		# print type(fileStr)
		# print hwLabels

		# print trainingFileList

handwritingClassTest()