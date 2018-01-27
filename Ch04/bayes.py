# -*-coding:utf-8-*-
from numpy import *
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

def trainNB0(trainMatrix,trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs)
	p0Num = zeros(numWords)
	p1Num = zeros(numWords)
	p0Denom = 0.0
	p1Denom = 0.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = p1Num/p1Denom
	p0Vect = p0Num/p0Denom
	return p0Vect,p1Vect,pAbusive

	
listOPosts,listClasses = lodaDataSet()
myVocabList = createVocabList(listOPosts)
Vec = setOfWords2Vec(myVocabList,listClasses)

trainMat = []
for postinDoc in listOPosts:
	trainMat.append(Vec)

trainNB0(trainMat,listClasses)