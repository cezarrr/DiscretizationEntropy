__author__ = 'CJank'

"""
Counts how many times each value occures
"""

import Loader
import copy
import math

def countOccurency(dataTable):
    listOfDicts = dict.fromkeys(xrange(len(dataTable[0])))
    for d in range(len(listOfDicts)):
        listOfDicts[d] = {}

    for row in dataTable:
        for columnNr in range(len(row)):
            columnVal = row[columnNr]
            if(listOfDicts[columnNr].get(columnVal)==None):
                listOfDicts[columnNr].update({columnVal:1})
            else:
                listOfDicts[columnNr][columnVal]=listOfDicts[columnNr].get(columnVal)+1

    return listOfDicts

def countProbabilities(listOfDicts):
    probDicts = copy.deepcopy(listOfDicts)

    for att in probDicts:
        sumOfVal = (sum (probDicts[att].itervalues()))
        for eachEntry in probDicts[att]:
            probDicts[att][eachEntry] = (float)(probDicts[att][eachEntry])/sumOfVal

    return  probDicts

def countEntropyOfDicts(probabilityDicts):
    entropyDicts = copy.deepcopy(probabilityDicts)

    for att in entropyDicts:
       for eachEntry in entropyDicts[att]:
            entropyDicts[att][eachEntry] = \
                (float)(entropyDicts[att][eachEntry]) * math.log((float)(entropyDicts[att][eachEntry]),2)

    return entropyDicts

def sumEntropyInSingleDict(inputEntropyDict):
    sumEntropy = (sum (inputEntropyDict.itervalues())) *(-1)
    return  sumEntropy

def countEntropyInData(entropyDict):
    sumEntropy=0.0
    for att in entropyDict:
        sumEntropy+=sumEntropyInSingleDict(entropyDict[att])
    meanEntropy=sumEntropy/len(entropyDict)
    return (sumEntropy,meanEntropy)

if __name__ == "__main__":
    file = "C:\Users\CJank\Desktop\\tmp\\wineDscr.arff"
    loadedData = Loader.loadExtensionSensitive(file)
    dicks=countOccurency(loadedData)
    pDics = countProbabilities(dicks)
    eDicts = countEntropyOfDicts(pDics)
    sumEnt, meanEnt = countEntropyInData(eDicts)
    print(dicks)
    print (pDics)
    print (eDicts)
    print ("Sum: "+(str)(sumEnt) +"    Mean: "+(str)(meanEnt)+"")