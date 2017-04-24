import random
import math

def chi_test(rand_num,bins):
    theoretical = len(rand_num)/bins
    numbers_in_bin = [0 for i in range(bins)]
    obs_diff_the = [0 for i in range(bins)]
    for i in rand_num:
        numbers_in_bin[int(i*10)] += 1

    for i in range(bins):
        obs_diff_the[i] = ((numbers_in_bin[i] - theoretical)**2) / theoretical

    summed = sum(obs_diff_the)
    return summed




def ks_test(rand_nums, size):
    obs_diff_the = [0 for i in range(len(rand_nums))]

    for i in range(size):
        counter = 0
        for j in range(size):
            if rand_num[i] <= i:
                counter += 1

        val = counter/size
        obs_diff_the[i] = math.fabs(val-rand_num[i])

    return max(obs_diff_the)




rand_num = []


print("How many numbers needed:")
howmany = int(input())

print("Number of bins:")
bins = int(input())


for i in range(howmany):
    rand_num.append(random.random())



print("Chi_test value %f" %chi_test(rand_num,bins))
print("KS_test value %f" %ks_test(rand_num,howmany))

