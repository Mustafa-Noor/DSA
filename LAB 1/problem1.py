def SearchA(Arr, x):
    indices = []
    for n in range(len(Arr)):
        if(Arr[n] == x):
            indices.append(n)
    return indices


Arr = [22, 2, 1, 7, 11, 13, 5, 2, 9]
target = 2

result = SearchA(Arr, target)
print("Index: ", result)