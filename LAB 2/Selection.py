from funcs import RandomArray
import time

# function implementing the selection sort
def SelectionSort(array, start, end):
    for i in range(start, end+1):
        for j in range(i+1, end+1):
            min = i
            if(array[j] < array[min]):
                array[j], array[min] = array[min], array[j]


# -----------------------------------------------------
# Driver code

n = 30000 # size of the array

# creates a random array
myArray = RandomArray(n) 
lastIndex = len(myArray) - 1

# this notes time
start_time = time.time()
SelectionSort(myArray, 0, lastIndex) # sort  
end_time = time.time()

# calculation of runtime
runtime = end_time - start_time 

# printing of the runtime
print("Runtime for Selection Sort is :  ", runtime, "seconds")


# this is for writing sorted array in csv file
f = open("SortedSelectionSort.csv", mode="w")
for i in myArray:
    f.write(str(i) + "\n")