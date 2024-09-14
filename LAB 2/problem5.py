from problem1 import RandomArray
def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(start,end - i + start):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]


rand = RandomArray(10)
print(rand)
BubbleSort(rand, 2, 7)
print(rand)