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


print(Sort10([10, -1, 9, 20, -3, -8, 22, 9, 7]))