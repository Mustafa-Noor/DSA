def SumIterative(number):
    sum = 0

    while number != 0:
        sum += number%10
        number = number//10

    return sum


print(SumIterative(1524))


def SumRecurive(number):
    if number == 0:
        return 0
    else:
        return number%10 + SumRecurive(number//10)
    
print(SumRecurive(1524))