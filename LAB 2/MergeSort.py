from funcs import RandomArray
import time

def MergeSort(array, start, end):
    if start >= end:
        return
    else:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)

def Merge(array, p, q, r):
    leftArray = array[p:q + 1]
    rightArray = array[q + 1:r + 1]

    i = 0
    j = 0
    mergedIndex = p

    # Merge the two arrays
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:  
            array[mergedIndex] = leftArray[i]
            i += 1
        else:
            array[mergedIndex] = rightArray[j]
            j += 1
        mergedIndex += 1

    # Copy the remaining elements of leftArray, if any
    while i < len(leftArray):
        array[mergedIndex] = leftArray[i]
        i += 1
        mergedIndex += 1

    # Copy the remaining elements of rightArray, if any
    while j < len(rightArray):
        array[mergedIndex] = rightArray[j]
        j += 1
        mergedIndex += 1

# -----------------------------------------------------
# Driver code

n = 30000 # size of the array

# creates a random array
myArray = RandomArray(n) 
lastIndex = len(myArray) - 1

# this notes time
start_time = time.time()
MergeSort(myArray, 0, lastIndex) # sort  
end_time = time.time()

# calculation of runtime
runtime = end_time - start_time 

# printing of the runtime
print("Runtime for Merge Sort is :  ", runtime, "seconds")


# this is for writing sorted array in csv file
f = open("SortedMergeSort.csv", mode="w")
for i in myArray:
    f.write(str(i) + "\n")

    