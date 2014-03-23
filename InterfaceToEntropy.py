__author__ = 'CJank'

import OccurencyCounter as oc
import InconsistencyCounter as ic
import os
import shlex

def writeResultsToFile(tupleToWrite, filePath):
    with open(filePath,'w+') as file:
        try:
            for tup in tupleToWrite:
                for field in range(len(tup)):
                    file.write( str(tup[field]))
                    if field<len(tup)-1:
                        file.write(",")
                    else:
                        file.write("\n")
        finally:
            file.close()


if __name__ == "__main__":
    paths = raw_input('Path to output file [space] paths to files with data to count entropy (space as delimiter): ').rstrip('\n')

    pathsList = shlex.split(paths, posix=False)
    pathsList = [x.lstrip('"').rstrip('"') for x in pathsList ]
    resultPath = pathsList[0]
    pathsList = pathsList[1:]


    results = []
    reductionOptions = [False,True]
    results.append(("File:","Reduction?"," Entropy: [bit]",\
                    "Number of instances:","Number of necessary attributes:","Number of values of attributes:",
                    "Minimal number of bits to save whole dataset:","Number of inconsistencies:",\
                    "Percent of inconsistencies:"))
    for tablePath in pathsList:
        for opt in reductionOptions:
            (sumE, meanE, metricE,bitsToSaveData,dataLen,numberOfAttsVal,numberOfImportantAtts)=\
                oc.loadAndCount(tablePath,reduceData=opt)
            inconsistencyCount, inconsistencyRatio = ic.countInconsistencyFromFile(tablePath,reduceData=opt)
            print (tablePath+"(reduction="+str(opt)+")"+" ->  Entropy: [bit] "+(str)(sumE)+ \
                   "  Minimal number of bits to save whole dataset: "+(str)(bitsToSaveData)+ \
                   "  Inconsistencies: "+(str)(inconsistencyCount)+\
                   " ("+str(inconsistencyRatio*100)+" %)")
            results.append((os.path.basename(tablePath),opt,sumE,dataLen,numberOfImportantAtts,numberOfAttsVal,\
                            bitsToSaveData,inconsistencyCount,inconsistencyRatio*100))
            writeResultsToFile(results,resultPath)
