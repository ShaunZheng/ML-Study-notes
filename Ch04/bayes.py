# -*-coding:utf-8-*-
def lodaDataSet():
	postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
			['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
			['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
			['stop', 'posting', 'stupid', 'worthless', 'garbage'],
			['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
			['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0,1,0,1,0,1] 
	return postingList,classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			# 通过index找到word在词汇表中的索引位置，并将该处设置为1
			returnVec[vocabList.index(word)] = 1
		else:
			print "这个%s单词不在我的词汇库中!" % word
	return returnVec


	
listOPosts,listClasses = lodaDataSet()
myVocabList = createVocabList(listOPosts)
print setOfWords2Vec(myVocabList,['a','b','c','d','b','c','d','b','c','d','b','c','d','b','c','d','b','c','d'])
print listOPosts[0].index('dog')