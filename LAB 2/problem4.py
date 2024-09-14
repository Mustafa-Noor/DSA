from problem1 import RandomArray
import time
n = 10
def HybridMergeSort(array, start, end):
    if(end-start + 1) <= n:
        InsertionSort(array, start, end)
    else:
        mid = (start + end) // 2
        HybridMergeSort(array, start, mid)
        HybridMergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
        


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


def InsertionSort(array, start, end):
    for i in range(start+1, end+1):
        key = array[i]
        j = i-1
        while(j >= start and array[j] > key):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    


myArray = RandomArray(11)
start_time = time.time()
print(myArray)
HybridMergeSort(myArray, 0, 10)
end_time = time.time()
runtime = end_time - start_time
print(myArray)