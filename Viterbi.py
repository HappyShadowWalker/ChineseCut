__author__ = 'ShadowWalker'
from numpy import *
import decimal, math
# 读取HMM模型参数
def preViterbi(transFileName, emitFileName):
    # 读取得到隐状态之间的转移概率矩阵
    tranFile = open(transFileName, 'r')
    transMatrix = arange(16, dtype = float64).reshape(4, 4)
    tranFileContent = tranFile.readlines()
    tranFile.close()
    i = -1
    for eachLine in tranFileContent:
        if eachLine[0] != '#':
            i = i + 1
            eachLineList = eachLine.split()
            for j in range(len(eachLineList)):
                transMatrix[i][j] = -float(eachLineList[j][1:len(eachLineList[j])])
    # 读取得到字典，和状态发射矩阵
    wordFile = open('worddict.txt', 'r')
    wordFileContent = wordFile.readlines()
    wordFile.close()
    worddict = []
    for i in range(len(wordFileContent)):
        line = wordFileContent[i]
        contentList = line.split()
        if contentList[0] == '#WordDict':
            wordContent = wordFileContent[i+1].split()
            for singleword in wordContent:
                worddict.append(singleword)

    # 读取emitFile 得到发射概率矩阵
    emitFile = open(emitFileName, 'r')
    emitFileContent = emitFile.readlines()
    emitFile.close()
    emitMatrix = arange(4 * len(worddict), dtype = float64).reshape(4, len(worddict))
    for i in range(len(emitFileContent)):
        line = emitFileContent[i]
        contentList = line.split()
        if contentList[0] == '#':
            if contentList[1] == 'B':
                BContent = emitFileContent[i+1].split()
                for j in range(len(BContent)):
                    emitMatrix[0][j] = -float(BContent[j][1:len(BContent[j])])
            if contentList[1] == 'M':
                MContent = emitFileContent[i+1].split()
                for j in range(len(MContent)):
                    emitMatrix[1][j] = -float(MContent[j][1:len(MContent[j])])
            if contentList[1] == 'E':
                EContent = emitFileContent[i+1].split()
                for j in range(len(EContent)):
                    emitMatrix[2][j] = -float(EContent[j][1:len(EContent[j])])
            if contentList[1] == 'S':
                SContent = emitFileContent[i+1].split()
                for j in range(len(SContent)):
                    emitMatrix[3][j] = -float(SContent[j][1:len(SContent[j])])
    print(transMatrix)
    print(emitMatrix)
    return transMatrix, emitMatrix, worddict

# 实现 Viterbi 算法
MinDouble = -10000000000000000
def viterbi(cutStr , iniProb, transMatrix, emitMatirx, wordDict):
    lenstr = len(cutStr)
    weight = arange(4 * lenstr, dtype=float64).reshape(4, lenstr)
    path = arange(4 * lenstr, dtype=float64).reshape(4, lenstr)
    weight[0][0] = iniProb[0] + emitMatirx[0][wordDict.index(cutStr[0])]
    weight[1][0] = MinDouble
    weight[2][0] = MinDouble
    weight[3][0] = iniProb[3] + emitMatirx[3][wordDict.index(cutStr[0])]
    for i in range(1, lenstr):
        for j in range(4):
            weight[j][i] = MinDouble
            path[j][i] = -1
            for k in range(4):
                temp = weight[k][i-1] + transMatrix[k][j] + emitMatirx[j][wordDict.index(cutStr[i])]
                print (temp)
                if temp > weight[j][i]:
                    weight[j][i] = temp
                    path[j][i] = k
    print(weight)
    print(path)
    # 对结果进行解码
    iniMaxWeight = weight[0][lenstr - 1]
    index = 0
    for i in range(1, 4):
        if weight[i][lenstr-1] > iniMaxWeight:
            iniMaxWeight = weight[i][lenstr-1]
            index = i
    print(index)
    ReverseState = []
    ReverseState.append(index)
    for j in range(1, lenstr):
        index = path[index][lenstr-j]
        ReverseState.append(index)
    NormalState = []
    for i in range(len(ReverseState)):
        NormalState.append(ReverseState[len(ReverseState)-i-1])
    print(NormalState)

    # 根据NormalState 分割字符串
    headIndex = 0
    endIndex = 0
    cutedResult = []
    for i in range(len(NormalState)):
        if NormalState[i] == 0.0:
            headIndex = i
        if NormalState[i] == 2.0:
            endIndex = i
            cutedResult.append(cutStr[headIndex: endIndex+1])
        if NormalState[i] == 3.0:
            cutedResult.append(cutStr[i])
    print(cutedResult)

# 测试算法
TransMatrix, EmitMatrix, WordDict = preViterbi("tran.txt", "emit.txt")
IniProb = [-0.26268660809250016, MinDouble, MinDouble, -1.4652633398537678]
viterbi("中国的改革开放和现代化建设", IniProb, TransMatrix, EmitMatrix, WordDict)


