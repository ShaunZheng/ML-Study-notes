from numpy import *

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	# print arrayOLines
	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines,3))
	# print returnMat
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
		# print line
		# print returnMat.min(1)
	return returnMat,classLabelVector
datingMat,labels = file2matrix('datingTestSet2.txt')

def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet, ranges, minVals

normMat, ranges, minVals = autoNorm(datingMat)

print normMat, ranges, minVals