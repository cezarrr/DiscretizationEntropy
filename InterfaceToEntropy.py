__author__ = 'CJank'

import OccurencyCounter as oc

if __name__ == "__main__":
    paths = raw_input('Paths to files with data to count entropy (space as delimiter): ').rstrip('\n')
    pathsList = paths.split()
    pathsList = [x.lstrip('"').rstrip('"') for x in pathsList ]

    print pathsList

    for tablePath in pathsList:
        (sumE, meanE, metricE)=oc.loadAndCount(tablePath)
        print (tablePath+" ->  Sum: "+(str)(sumE)+"[bits]")