from funcs import RandomArray; # importing function for random array
import time

# insertion sort function (Problem 2)
def InsertionSort(array, start, end):
    for i in range(start+1, end+1):
        key = array[i]
        j = i-1
        while(j >= start and array[j] > key):
            array[j+1] = array[j] 
            j = j-1
        array[j+1] = key


# -----------------------------------------------------
# Driver code

n = 30000 # size of the array

# creates a random array
myArray = RandomArray(n) 
lastIndex = len(myArray) - 1

# this notes time
start_time = time.time()
InsertionSort(myArray, 0, lastIndex) # sort  
end_time = time.time()

# calculation of runtime
runtime = end_time - start_time 

# printing of the runtime
print("Runtime for Insertion Sort is :  ", runtime, "seconds")


# this is for writing sorted array in csv file
f = open("SortedInsertionSort.csv", mode="w")
for i in myArray:
    f.write(str(i) + "\n")
