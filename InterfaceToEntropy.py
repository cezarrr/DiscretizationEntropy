__author__ = 'CJank'

import OccurencyCounter as oc
import InconsistencyCounter as ic

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

    pathsList = paths.split()
    pathsList = [x.lstrip('"').rstrip('"') for x in pathsList ]
    resultPath = pathsList[0]
    pathsList = pathsList[1:]


    results = []
    options = [False,True]
    results.append(("Path of file:","Reduction?","Mean number of bits to save one instance:",\
                    "Bits to save the whole dataset:","Number of inconsistencies:"))
    for tablePath in pathsList:
        for opt in options:
            (sumE, meanE, metricE,bitsToSaveData)=oc.loadAndCount(tablePath,reduceData=opt)
            inconsistencyCount = ic.countInconsistencyFromFile(tablePath,reduceData=opt)
            print (tablePath+"(reduction="+str(opt)+")"+" ->  Mean number of bits to save one instance: "+(str)(sumE)+ \
                   "  Bits to save whole dataset: "+(str)(bitsToSaveData)+ \
                   "  Inconsistencies: "+(str)(inconsistencyCount))
            results.append((tablePath,opt,sumE,bitsToSaveData,inconsistencyCount))
            writeResultsToFile(results,resultPath)
