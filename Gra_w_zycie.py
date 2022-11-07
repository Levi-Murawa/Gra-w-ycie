# to start with, we will need matplotlib.pyplot
from matplotlib import pyplot as plt
import random
import time
# next, i will set up a 8 x 8 2d matrix, with random bits as elements (0 or 1);
# for randomization of integers (0 or 1) I use the random module in Python;
# for building each row in the 2d matrix I use list comprehension in Python

plt.ion()
x = 10
y = 10

for i in range(10):
    data = [[random.randint(a=0,b=1) for x in range(0,x)], # row 1
            [random.randint(a=0,b=1) for x in range(0,x)], # row 2
            [random.randint(a=0,b=1) for x in range(0,x)], # row 3
            [random.randint(a=0,b=1) for x in range(0,x)], # row 4
            [random.randint(a=0,b=1) for x in range(0,x)], # row 5
            [random.randint(a=0,b=1) for x in range(0,x)], # row 6
            [random.randint(a=0,b=1) for x in range(0,x)], # row 7
            [random.randint(a=0,b=1) for x in range(0,x)]] # row 8
    plt.imshow(data)
    plt.pause(0.5)
    plt.clf()

