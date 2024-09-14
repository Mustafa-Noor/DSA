from problem1 import RandomArray
def SelectionSort(array, start, end):
    for i in range(start, end+1):
        for j in range(i+1, end+1):
            min = i
            if(array[j] < array[min]):
                array[j], array[min] = array[min], array[j]

rand = RandomArray(10)
print(rand)
SelectionSort(rand, 2, 7)
print(rand)