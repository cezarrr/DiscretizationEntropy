__author__ = 'CJank'

"""
Counts how many times each value occures
"""

import Loader
import copy

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

if __name__ == "__main__":
    file = "C:\Users\CJank\Desktop\\tmp\\wineDscr.arff"
    loadedData = Loader.loadExtensionSensitive(file)
    dicks=countOccurency(loadedData)
    pDics = countProbabilities(dicks)
    print(dicks)
    print (pDics)