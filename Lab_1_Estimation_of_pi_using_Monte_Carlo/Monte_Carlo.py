import random
import numpy as np
import matplotlib.pyplot as plt


### This link:"http://mathfaculty.fullerton.edu/mathews/n2003/montecarlopimod.html" describes
### the theorem behind pi estimation Using Monte Carlo

### In Monte Carlo Simulation we are going to simulate pi value from probability theorem. We are considering a
### circular field which is surrounded by a rectangle. First of all we are going to simulate Raindrops from uniform
### distribution. The default Random.Random() function returns values which are uniformly distributed. After getting
### the co-ordinates of raindrops we are going to calculate if the raindrop is faliing inside the circle or outside.
### After getting the numbers of raindrops inside and outside the circle we can estimate value of Pi..



num_of_raindrops = 10000
batch = 100   # At a time 100 drops can fall. So batch represent number of raindrops at t.
outer_loop = int(num_of_raindrops / batch)


in_circle_x = []
out_circle_x = []
in_circle_y = []
out_circle_y = []


circle = plt.Circle((0, 0), radius=0.5, color='BLACK', fill=False)  # Drawing the circle field which has radius .5
ax = plt.gca()
ax.add_artist(circle)


for j in range(outer_loop):
    for i in range(batch):
        x = .5 - random.random() # Generating X co-ordinate of raindrop
        y = .5 - random.random() # Generating Y co-ordinate of raindrop

        if x**2 + y**2 <= .25:   # Checking if the raindrop is falling inside the circle
            in_circle_x.append(x)
            in_circle_y.append(y)
        else:
            out_circle_x.append(x)
            out_circle_y.append(y)

    plt.figure(1)     # plot1 simulates raindrops
    plt.scatter(in_circle_x,in_circle_y,c='b')
    plt.scatter(out_circle_x,out_circle_y,c='r')
    plt.pause(.0001)


    pi = 4 * (len(in_circle_x)/ (len(in_circle_x) + len(out_circle_x)) )
    plt.figure(2)   # plot2 shows the estimation of Pi with respect to time
    plt.hlines(np.pi,0,outer_loop)  # For showing real value of Pi
    plt.scatter(j,pi)
    plt.title("%s" %(pi))
    plt.ylim(3.01,3.99)
    plt.pause(.0001)

plt.show()
