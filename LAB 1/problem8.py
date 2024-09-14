def SortedMerge(Arr1, Arr2):
    sortedArr = []
    while Arr1 and Arr2:
        if Arr1[0] <= Arr2[0]:
            sortedArr.append(Arr1[0])
            Arr1.pop(0)
        else:
            sortedArr.append(Arr2[0])
            Arr2.pop(0)
    while Arr1:
        sortedArr.append(Arr1[0])
        Arr1.pop(0)

    while Arr2:
        sortedArr.append(Arr2[0])
        Arr2.pop(0)

    return sortedArr


print(SortedMerge([0,3,4,10,11],[1,8,13,24]))