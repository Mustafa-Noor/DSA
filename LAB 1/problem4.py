def Minimum(Arr, starting, ending):
    minIndex = starting

    for n in range(starting, ending + 1):
        if(Arr[n] < Arr[minIndex]):
            minIndex = n

    return minIndex

def Sort4(Arr):
    Array = []
    while len(Arr):
        indexSmallest = Minimum(Arr, 0, len(Arr)-1)
        Array.append(Arr[indexSmallest])
        Arr.pop(indexSmallest)
    return Array


print(Sort4([3,4,7,8,0,1,23,-2,-5]))
