print("Give a:")
a = int(input())
print("Give c:")
c = int(input())
print("Give m:")
m = int(input())

import numpy as np
import random
import math

def prime(m):
    primes = []
    for i in range(2, m):
        Flag = True
        for j in range(2,i):
            if i % j == 0:
                Flag = False
        if Flag == True: primes.append(i)
    return primes


def check(a,c,m):
    if math.gcd(c,m) != 1:
        return False
    primes = prime(m)

    for i in primes:
        if m%i==0:
            if (a - 1) % i!=0:
                return False

    if m%4==0 and (a-1)%4!=0:
        return False

    return True


if check(a,c,m)==True:
    print("Condition Satisfied")
else:
    print("Condition not Satisfied")



def ranNumGen(z0,a,c,m):
    zNum = z0
    while True:
        zNew = ((a * zNum) + c) % m
        zNum = zNew
        yield zNew

z = 7


for j in range(z):
    numbers = []
    for i in ranNumGen(j, a, c, m):
        if i not in numbers:
            numbers.append(i)
        else:
            break
    print(len(numbers))

numbers2 = []
for i in numbers:
    numbers2.append(i/m)


numbers3=[]
for i in range(len(numbers2)):
    numbers3.append(random.uniform(0,1))

print(*numbers3)

import matplotlib.pyplot as plt
plt.hist(x=numbers2,bins=5,normed=True,alpha=0.5)
plt.hist(x=numbers3,bins=5,normed=True,color='r',alpha=0.5)
plt.show()