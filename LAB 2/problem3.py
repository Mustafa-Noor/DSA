from problem1 import RandomArray
import time

def MergeSort(array, start, end):
    if start >= end:
        return
    else:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
        return array

def Merge(array, p, q, r):
    leftArray = array[p:q + 1]
    rightArray = array[q + 1:r + 1]

    i = 0
    j = 0
    k = p

    # Merge the two arrays
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:  # Fixed to maintain stability
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    # Copy the remaining elements of leftArray, if any
    while i < len(leftArray):
        array[k] = leftArray[i]
        i += 1
        k += 1

    # Copy the remaining elements of rightArray, if any
    while j < len(rightArray):
        array[k] = rightArray[j]
        j += 1
        k += 1


myArray = RandomArray(30000)
start_time = time.time()
sortedArr = MergeSort(myArray, 0, 30000)
end_time = time.time()
runtime = end_time - start_time
print(sortedArr)


print("Runtime for Merge Sort is :  ", runtime, "seconds")

f = open("SortedMergeSort.csv", mode="w")
for i in sortedArr:
    f.write(str(i) + "\n")