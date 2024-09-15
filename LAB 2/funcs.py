import random
def RandomArray(size):
    randomNumbers = []
    for i in range(0,size):
        rand  = random.randint(0, 1000)
        randomNumbers.append(rand)
    return randomNumbers

#
