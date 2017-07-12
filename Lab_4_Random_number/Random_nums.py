import random
import math
import numpy as np

def Bernoulli(prob):
    num = random.uniform(0,1)
    if num<=prob:
        return 1
    return  0



def Geometric(prob):
    count = 0
    while True:
        num = random.uniform(0, 1)
        if num <= prob:
            break
        count += 1
    return count


def Binomial(n,prob):
    count = 0
    for i in range(n):
        if Bernoulli(prob) == 1:
            count += 1

    return count


def Expo(lambd):
    num = random.uniform(0,1)
    return -(np.log((1-num))/lambd)




print(Bernoulli(.44))
print(Geometric(.65))
print(Binomial(10,.3))
print(Expo(2))