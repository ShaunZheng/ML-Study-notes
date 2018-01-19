from numpy import *

import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
	# 
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	# 
	sortedDistIndicies = distances.argsort()
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