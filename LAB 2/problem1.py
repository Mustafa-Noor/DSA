import random
def RandomArray(size):
    randomNumbers = []
    for i in range(size):
        rand  = random.randint(0, 1000)
        randomNumbers.append(rand)
    return randomNumbers

#
