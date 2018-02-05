# Python Implementation of Insertion Sort algorithm

def InsertionSort(numList):
    for j in range(1,len(numList)):
        key = numList[j]
        i = j-1
        while i >= 0 and numList[i] > key:
            numList[i+1] = numList[i]
            i = i-1
        numList[i+1] = key
    return numList

import numpy as np

data = np.loadtxt("numbers/5_numbers.txt")

sortedList = InsertionSort(data)

np.savetxt("sorted.txt", sortedList, fmt="%d")
