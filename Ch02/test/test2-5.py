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
