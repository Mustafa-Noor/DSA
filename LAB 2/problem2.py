from problem1 import RandomArray;
import time

def InsertionSort(array, start, end):
    for i in range(start, end):
        key = array[i]
        j = i-1
        while(j >= start and array[j] > key):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array


myArray = RandomArray(30000)
start_time = time.time()
sortedArr = InsertionSort(myArray, 0, 30000)
end_time = time.time()
runtime = end_time - start_time
print(sortedArr)


print("Runtime for Insertion Sort is :  ", runtime, "seconds")

# f = open("SortedInsertion.csv", mode="w")
# for i in sortedArr:
#     f.write(str(i) + "\n")
