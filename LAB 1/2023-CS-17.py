#   Problem 1
def SearchA(Arr, x):
    indices = []
    for n in range(len(Arr)):
        if(Arr[n] == x):
            indices.append(n)
    return indices
#   Driver Code Problem 1
Arr = [22, 2, 1, 7, 11, 13, 5, 2, 9]
target = 2

result = SearchA(Arr, target)
print("Index: ", result)

#------------------------------------------

#   Problem 2
def SearchB(Arr, x):
    indices = []
    i = 0
    
   
    if x < Arr[0]:
        return indices 
    elif x > Arr[len(Arr) - 1]:
        return indices

    
    while Arr[i] <= x:
        if Arr[i] == x:
            indices.append(i)
        i += 1
    
    return indices
#   Driver Code Problem 2
Arr = [1,2,2,5,7,9,11,13,22]
target = 2

print("Index: ", SearchB(Arr, target))

#------------------------------------------

#   Problem 3
def Minimum(Arr, starting, ending):
    minIndex = starting

    for n in range(starting, ending + 1):
        if(Arr[n] < Arr[minIndex]):
            minIndex = n

    return minIndex
#   Driver Code Problem 3
Array= [3,4,7,8,0,1,23,-2,-5]
StartingIndex= 4
EndingIndex= 7
print(Minimum(Array, StartingIndex, EndingIndex))

#------------------------------------------

#   Problem 4
def Sort4(Arr):
    Array = []
    while len(Arr):
        indexSmallest = Minimum(Arr, 0, len(Arr)-1)
        Array.append(Arr[indexSmallest])
        Arr.pop(indexSmallest)
    return Array
#   Driver Code Problem 4
print("X = ", Sort4([3,4,7,8,0,1,23,-2,-5]))

#------------------------------------------

#   Problem 5
def StringReverse(str, starting, ending):
    res = ""
    for i in range(ending-1,starting-1, -1):
        res += str[i]
    return res
#   Driver Code Problem 5
s = "University of Engineering and Technology Lahore"
print(StringReverse(s, 27, 40))

#------------------------------------------

#   Problem 6
def SumIterative(number):
    sum = 0

    while number != 0:
        sum += number%10
        number = number//10

    return sum
def SumRecurive(number):
    if number == 0:
        return 0
    else:
        return number%10 + SumRecurive(number//10)
#   Driver Code Problem 6
print("Sum of digits is: ", SumIterative(1524))
print("Sum of digits is: ", SumRecurive(1524))

#-----------------------------------------

#   Problem 7
def ColumnWiseSum(Mat):
    numColumns  = len(Mat[0])
    columnsSum = [0]*numColumns

    for row in Mat:
        for elem in range(numColumns):
            columnsSum[elem] += row[elem]
    
    return columnsSum
def RowWiseSum(Mat):
    rowSum = []
    sum = 0
    for row in Mat:
        for elem in row:
            sum += elem
        rowSum.append(sum)
        sum = 0
    return rowSum
# Driver Code Problem 7
print("Row-wise: ", RowWiseSum([[1,13 ,13],[5, 11, 6],[4, 4, 9]]))
print("Column-wise: ", ColumnWiseSum([[1,13 ,13],[5, 11, 6],[4, 4, 9]]))

#-----------------------------------------

#   Problem 8
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
#   Driver Code Problem 8
print(SortedMerge([0,3,4,10,11],[1,8,13,24]))

#-----------------------------------------

#   Problem 9
def PalindromRecursive(str):
    if len(str) <= 1:
        return True
    elif str[0] == str[-1]:
        return PalindromRecursive(str[1:-1])
    else:
        return False
#   Driver Code Problem 9
print(PalindromRecursive("radar"))

#-----------------------------------------

#   Problem 10
def Sort10(Arr):
    resArr = []
    positiveNumbers = []
    negativeNumbers = []

    for num in Arr:
        if num < 0:
            negativeNumbers.append(num)
        else:
            positiveNumbers.append(num)

    positiveNumbers = sorted(positiveNumbers)
    negativeNumbers = sorted(negativeNumbers)

    while negativeNumbers:
        resArr.append(negativeNumbers[0])
        negativeNumbers.pop(0)
        if positiveNumbers:
            resArr.append(positiveNumbers[0])
            positiveNumbers.pop(0)

    while positiveNumbers:
        resArr.append(positiveNumbers[0])
        positiveNumbers.pop(0)


    return resArr
#   Driver Code Problem 10
print(Sort10([10, -1, 9, 20, -3, -8, 22, 9, 7]))
