from funcs import RandomArray
import time

# function implementing bubble sort
def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(start,end - i + start):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]


# -----------------------------------------------------
# Driver code

n = 30000 # size of the array

# creates a random array
myArray = RandomArray(n) 
lastIndex = len(myArray) - 1

# this notes time
start_time = time.time()
BubbleSort(myArray, 0, lastIndex) # sort  
end_time = time.time()

# calculation of runtime
runtime = end_time - start_time 

# printing of the runtime
print("Runtime for Bubble Sort is :  ", runtime, "seconds")


# this is for writing sorted array in csv file
f = open("SortedBubbleSort.csv", mode="w")
for i in myArray:
    f.write(str(i) + "\n")