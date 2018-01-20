# -*-coding:utf-8-*-
from numpy import *

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	# print arrayOLines
	# print type(arrayOLines)

	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines,3))
	# print numberOfLines
	# print returnMat
	# print type(returnMat)
	
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		# 除去空格换行等，注意内部的无法除去，只能除去开头结尾部分的
		line = line.strip()
		# print line
		# print type(line)

		listFromLine = line.split('\t')
		# print listFromLine

		# 循环将listFromLine每行前三列的值赋值给returnMat的每一行
		returnMat[index,:] = listFromLine[0:3]
		# print listFromLine[-1]
		# print type(listFromLine[-1])
		classLabelVector.append(int(listFromLine[-1]))
		index += 1

		# print returnMat.min(1)
	return returnMat,classLabelVector
datingMat,labels = file2matrix('datingTestSet2.txt')

# 归一化数值公式：newvalue = (oldvalue-min)/(max-min)
def autoNorm(dataSet):
	# 求得每列的最小值和最大值最后结果是[ 0.        0.        0.001156][  9.12730000e+04   2.09193490e+01   1.69551700e+00]
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	# print minVals
	# print maxVals
	
	# max-min
	ranges = maxVals - minVals
	# shape(dataSet)得到dataSet是几行几列的
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	# oldvalue-min
	normDataSet = dataSet - tile(minVals,(m,1))
	# newvalue
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet, ranges, minVals

normMat, ranges, minVals = autoNorm(datingMat)

print normMat, ranges, minVals