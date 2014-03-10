__author__ = 'CJank'

"""
Loading module
"""


import numpy as np
import pylab as pl
import csv

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
                        if columnParsed:
                            rowParsed.append(columnParsed)
                    if rowParsed!='':
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

if __name__ == "__main__":
    print(__doc__)
    file = "C:\Users\CJank\Desktop\\tmp\\testowyRSES.tab"
    file2 = "C:\Users\CJank\Desktop\\tmp\\wineDscr.arff"
    X=loadExtensionSensitive(file2)
    print X