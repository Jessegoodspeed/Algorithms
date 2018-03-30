# Python Implementation of Insertion Sort algorithm
# This is one of the O(n^2) time sorting algorithms that sorts by comparing individual elements with another.

import numpy as np

def InsertionSort(numList):
    for j in range(1,len(numList)):
        key = numList[j]
        i = j-1
        while i >= 0 and numList[i] > key:
            numList[i+1] = numList[i]
            i = i-1
        numList[i+1] = key
    return numList

# Input txt file into data
data = np.loadtxt("numbers/5_numbers.txt")

# Sort data
sortedList = InsertionSort(data)

# Save data to another txt file
np.savetxt("sorted.txt", sortedList, fmt="%d")
