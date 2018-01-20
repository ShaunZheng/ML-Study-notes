# 不可独立运行

def datingClassTest():
	hoRatio = 0.10
	
	datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print "分类结果：%d,真实值：%d" % (classifierResult,datingLabels[i])
		if (classifierResult != datingLabels[i]):
			errorCount +=1.0
	print 'b'
	print "a :%f" % (errorCount/float(numTestVecs))

datingClassTest()