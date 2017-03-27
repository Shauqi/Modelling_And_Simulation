import random
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.ion()
circle = plt.Circle((0, 0), radius=0.5, color='k', fill=False)
ax = plt.gca()
ax.add_artist(circle)
plt.show()
plt.figure(2)
plt.ion()
plt.show()

# style.use('fivethirtyeight')

raindrops_num = 1000
at_a_time_drop =100
x_in_circle = []
y_in_circle = []
x_out_circle = []
y_out_circle = []


for i in range(int(raindrops_num/at_a_time_drop)):
    for j in range(at_a_time_drop):
        x = .5-random.random()
        y = .5-random.random()

        if x**2+y**2 <=.25:
            x_in_circle.append(x)
            y_in_circle.append(y)
        else:
            x_out_circle.append(x)
            y_out_circle.append(y)

    plt.figure(1)
    plt.scatter(x_in_circle, y_in_circle, label='in_circle', c='b')
    plt.scatter(x_out_circle, y_out_circle, label='out_circle', c='r')
    plt.title("%s drops: %s landed in circle" %(raindrops_num, len(x_in_circle)))
    plt.draw()
    plt.pause(.0001)

    plt.figure(2)
    pi = 4*(len(x_in_circle)/(len(x_in_circle)+len(x_out_circle)))
    plt.hlines(np.pi, 0, int(raindrops_num/at_a_time_drop))
    plt.scatter(i, pi)
    plt.ylim(3.0, 3.2)
    plt.xlabel("Number of rain drops / 100")
    plt.ylabel("$\pi$")
    plt.title("Estimating $\pi$ as %s" %(pi))
    plt.draw()
    plt.pause(.0001)

plt.pause(10)