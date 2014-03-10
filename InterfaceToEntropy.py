__author__ = 'CJank'

import OccurencyCounter as oc
import InconsistencyCounter as ic

if __name__ == "__main__":
    paths = raw_input('Paths to files with data to count entropy (space as delimiter): ').rstrip('\n')
    pathsList = paths.split()
    pathsList = [x.lstrip('"').rstrip('"') for x in pathsList ]

    for tablePath in pathsList:
        (sumE, meanE, metricE,bitsToSaveData)=oc.loadAndCount(tablePath,reduceData=True)
        inconsistencyCount = ic.countInconsistencyFromFile(tablePath)
        print (tablePath+" ->  Mean number of bits to save one instance: "+(str)(sumE)+"  Bits to save whole dataset: "+(str)(bitsToSaveData)+ \
               "  Inconsistencies: "+(str)(inconsistencyCount))