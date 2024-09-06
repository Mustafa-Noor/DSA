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


Arr = [1,2,2,3,3,4,5,6,7,8,9]
target = 3

print(SearchB(Arr, target))