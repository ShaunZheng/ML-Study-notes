from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelsCounts = {}
	for featVec in dataSet:
		print featVec
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

myDat,labels = createDataSet()

print myDat
print calcShannonEnt(myDat)