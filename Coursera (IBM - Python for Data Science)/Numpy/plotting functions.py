import time
import sys
import numpy as np
import matplotlib.pyplot as plt


def Plotvec1(u, z, v):

    ax = plt.axes()  # to generate the full window axes
    # Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')  # Adds the text u to the Axes

    # Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')  # Adds the text v to the Axes

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')  # Adds the text z to the Axes
    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)
    plt.show()


u = np.array([1, 0])
print(u)

v = np.array([0, 1])
print(v)

z = np.add(u, v)
print(z)

Plotvec1(u, z, v)
