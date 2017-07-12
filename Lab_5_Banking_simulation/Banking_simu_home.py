import random
import simpy
import matplotlib.pyplot as plt


INTERVAL_CUSTOMERS = 10

X = []
Y = []
X.append(0)
Y.append(0)

cus_counter = 0

def source(env, interval, counter):
    customer_count = 0
    while True:
        c = customer(env, 'Customer%02d' % customer_count, counter, time_in_bank=12)
        env.process(c)
        # t = random.expovariate(1.0/ interval)
        yield env.timeout(interval)
        customer_count += 1


def customer(env, name, counter, time_in_bank):
    arrive = env.now
    print('%7.4f %s: Here I am' % (arrive, name))
    with counter.request() as req:
        yield req
        wait = env.now - arrive
        if wait > 0:
            global cus_counter
            cus_counter += 1
            X.append(arrive)
            Y.append(cus_counter)
            cus_counter -= 1
        print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))
        # tib = random.expovariate(1.0 / time_in_bank)
        yield env.timeout(time_in_bank)
        print('%7.4f %s: Finished' % (env.now, name))
        X.append(env.now)
        Y.append(cus_counter)

print('Bank System')


env = simpy.Environment()

counter = simpy.Resource(env, capacity=1)
env.process(source(env, INTERVAL_CUSTOMERS, counter))
env.run(until=100)


X_sort = [x for (x,y) in sorted(zip(X,Y))]
Y_sort = [y for (x,y) in sorted(zip(X,Y))]

print(X_sort)
print(Y_sort)

prob = []
denomenator = 0
for i in range(0,max(Y_sort)+1):
    prob.append(0)
    denomenator += i


for i in range(0,len(Y)):
    if i == len(Y)-1:
        prob[Y_sort[i]] += 100 - X_sort[i]
    else:
        prob[Y_sort[i]] += X_sort[i + 1] - X_sort[i]


print(prob)

numerator = 0
for i in range(0,len(prob)):
    numerator += i * prob[i]



print(numerator/denomenator)



plt.bar(X,Y)
plt.legend(pos="best")
plt.xlabel("Time")
plt.ylabel("Number of persons waiting in the queue")
plt.show()
