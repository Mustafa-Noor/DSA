def ColumnWiseSum(Mat):
    numColumns  = len(Mat[0])
    columnsSum = [0]*numColumns

    for row in Mat:
        for elem in range(numColumns):
            columnsSum[elem] += row[elem]
    
    return columnsSum


print(ColumnWiseSum([[1,13 ,13],[5, 11, 6],[4, 4, 9]]))


def RowWiseSum(Mat):
    rowSum = []
    sum = 0
    for row in Mat:
        for elem in row:
            sum += elem
        rowSum.append(sum)
        sum = 0
    return rowSum


print(RowWiseSum([[1,13 ,13],[5, 11, 6],[4, 4, 9]]))