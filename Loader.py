__author__ = 'CJank'

"""
Loading module
"""


import csv
import copy

def loadData(fileName, csvDelimiter=','):
    dataSet = []
    with open(fileName, 'rb') as csvFile:
        try:
            csvR = csv.reader(csvFile, delimiter=csvDelimiter, quotechar='"')
            for row in csvR:
                if row:
                    rowParsed = []
                    for column in row:
                        try:
                            columnParsed = float(column)
                        except:
                            columnParsed = column
                        rowParsed.append(columnParsed)
                    dataSet.append(rowParsed)
        finally:
            csvFile.close()
    return dataSet

def loadDataTab(fileName, csvDelimiter=' '):
    dataSet = []
    with open(fileName, 'rb') as csvFile:
        try:
            startParsing = False
            csvR = csv.reader(csvFile, delimiter=csvDelimiter, quotechar='"')
            for row in csvR:
                if row:
                    rowParsed = []
                    for column in row:
                        if(startParsing==False and column!='OBJECTS'):
                            break
                        elif(startParsing==False and column=='OBJECTS'):
                            startParsing=True
                            break

                        try:
                            columnParsed = float(column)
                        except:
                            columnParsed = column
                        if columnParsed!='':
                            rowParsed.append(columnParsed)
                    if rowParsed:
                        dataSet.append(rowParsed)
        finally:
            csvFile.close()
    return dataSet

def loadDataArff(fileName, csvDelimiter=','):
    dataSet = []
    with open(fileName, 'rb') as csvFile:
        try:
            startParsing = False
            csvR = csv.reader(csvFile, delimiter=csvDelimiter, quotechar='"')
            for row in csvR:
                if row:
                    rowParsed = []
                    for column in row:
                        if(startParsing==False and column.upper()!='@DATA'):
                            break
                        elif(startParsing==False and column.upper()=='@DATA'):
                            startParsing=True
                            break

                        try:
                            columnParsed = float(column)
                        except:
                            columnParsed = column
                        if columnParsed!='':
                            rowParsed.append(columnParsed)
                    if rowParsed:
                        dataSet.append(rowParsed)
        finally:
            csvFile.close()
    return dataSet

def loadExtensionSensitive(fileName):
    loadedData=[]
    if (fileName.lower().endswith('.tab')):
        loadedData=loadDataTab(fileName)
    elif (fileName.lower().endswith('.arff')):
        loadedData=loadDataArff(fileName)
    else:
        loadedData=loadData(fileName)
    return loadedData

def checkIfRepetitionOccurs(instanceA, instanceB):
    numberOfAtts = len(instanceA)
    repetition = True
    for col in range(numberOfAtts):
        if(col< numberOfAtts):
            if(instanceA[col]!=instanceB[col]):
                repetition = False
                break
    return repetition

def reduceRepetitions(loadedData):
    currentData = copy.deepcopy(loadedData)
    a=0
    while a < len(currentData)-1:

        b=min(a+1,len(currentData)-1)
        while b < len(currentData):
            if(checkIfRepetitionOccurs(currentData[a],currentData[b])):
                del currentData[b]

            else:
                b+=1

        a+=1

    print ("Current len="+(str)(len(currentData)))
    print ("One-over-reduction ratio="+(str)((float)(len(currentData))/(float)(len(loadedData))))
    return currentData



if __name__ == "__main__":
    file = "C:\Users\CJank\Desktop\\tmp\ResultsOthers\irisWEKA.arff"

    X=loadExtensionSensitive(file)
    print X
    print len(X)
    Y = reduceRepetitions(X)
    print len(Y)