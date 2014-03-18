__author__ = 'CJank'

import Loader

def countInconsistency(loadedData):
    knownInconsistencies = set()
    for a in range(len(loadedData)-1):
        if(a in knownInconsistencies): #jesli juz policzylismy dla danej wartosci
                continue
        consistent = True
        for b in range(min(a+1,len(loadedData)-1),len(loadedData)):
            if(checkIfInconsistencyOccurs(loadedData[a],loadedData[b])):
                knownInconsistencies.add(a)
                knownInconsistencies.add(b)
    return len(knownInconsistencies)

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
    inconsistencyRatio = float(inconsistencyCounter)/len(data)
    return inconsistencyCounter, inconsistencyRatio

if __name__ == "__main__":
    data=Loader.loadExtensionSensitive("C:\Users\CJank\Desktop\Dyskretyzator\Results_\\australianDiscretizationResults_Reduced.txt")
    c=countInconsistency(data)
    print c