__author__ = 'CJank'

import Loader

def countInconsistency(loadedData):
    counter=0
    for a in range(len(loadedData)-1):
        for b in range(min(a+1,len(loadedData)-1),len(loadedData)):
            if(checkIfInconsistencyOccurs(loadedData[a],loadedData[b])):
                counter+=1
    return counter

def checkIfInconsistencyOccurs(instanceA, instanceB):
    numberOfAtts = len(instanceA)
    inconsistency = False
    for col in range(numberOfAtts):
        if(col< numberOfAtts-1):
            if(instanceA[col]!=instanceB[col]):
                break
        else:
            if(instanceA[col]!=instanceB[col]):
                inconsistency=True
    return inconsistency

def countInconsistencyFromFile(path, reduceData=False):
    data=Loader.loadExtensionSensitive(path)
    if (reduceData):
        data = Loader.reduceRepetitions(data)
    inconsistencyCounter=countInconsistency(data)
    return inconsistencyCounter

if __name__ == "__main__":
    data=Loader.loadExtensionSensitive("C:\Users\CJank\Desktop\Dyskretyzator\Results_\\australianDiscretizationResults_Reduced.txt")
    c=countInconsistency(data)
    print c