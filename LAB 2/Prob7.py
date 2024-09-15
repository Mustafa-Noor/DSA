from funcs import RandomArray
import csv
from Bubble import BubbleSort
from Insertion import InsertionSort
from MergeSort import MergeSort
from HybridMerge import HybridMergeSort
from Selection import SelectionSort
import time

# this function read values from Nvalues.txt
def ReadNvalues():
    numbersFile = open(file='Nvalues.txt', mode='r')
    lines = numbersFile.read()
    arraySizes = []
    numbers = lines.split()
    for n in numbers:
        num = int(n)
        arraySizes.append(num)
    return arraySizes

# function to calculate the runtime of sorting functions
def CalculateRuntime(sortFunction, myArray, start, end):
    start_time = time.time()
    sortFunction(myArray, start, end)
    end_time = time.time()
    runtime = end_time - start_time 
    return runtime


f = open("Runtime.csv", mode="w")
writer = csv.writer(f)
# this writes the header of the file 
writer.writerow(["Value of n", "Insertion sort (seconds)", "Merge sort (seconds)", "Hybrid Merge sort (seconds)", "Selection sort (seconds)", "Bubble sort (seconds)"])


arraySizes = ReadNvalues()
for n in arraySizes:
    randArray = RandomArray(n)
    lastIndex = len(randArray) - 1

    # this is for insertion sort time
    arrayCopy = randArray.copy()
    insertionTime = CalculateRuntime(InsertionSort, arrayCopy, 0, lastIndex)

    # this is for merge sort time
    arrayCopy = randArray.copy()
    mergeSortTime = CalculateRuntime(MergeSort, arrayCopy, 0, lastIndex)


    # this is for Hybrid Merge sort time
    arrayCopy = randArray.copy()
    hybridTime = CalculateRuntime(HybridMergeSort, arrayCopy, 0, lastIndex)


    # this is for selection sort time
    arrayCopy = randArray.copy()
    selectionTime = CalculateRuntime(SelectionSort, arrayCopy, 0, lastIndex)

    # this is for bubble sort time
    arrayCopy = randArray.copy()
    bubbleTime = CalculateRuntime(BubbleSort, arrayCopy, 0, lastIndex)

   # this writes the lines in runtime csv file
    writer.writerow([n, insertionTime, mergeSortTime, hybridTime, selectionTime, bubbleTime])








