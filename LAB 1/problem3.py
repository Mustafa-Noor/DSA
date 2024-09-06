def Minimum(Arr, starting, ending):
    minIndex = starting

    for n in range(starting, ending + 1):
        if(Arr[n] < Arr[minIndex]):
            minIndex = n

    return minIndex

Array= [3,4,7,8,0,1,23,-2,-5]
StartingIndex= 4
EndingIndex= 7
print(Minimum(Array, StartingIndex, EndingIndex))