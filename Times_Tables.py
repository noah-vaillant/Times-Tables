#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:44:25 2024

@author: noahvaillant
"""



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter as w


# The idea behind this code is to set up a circle of points where every point
# has an integer value and applying a factor to them all to see where they
# end up graphically. I take the remainder of the outputted value of every point
# with the amount of points on the circle and plot the output back on the circle.
# This gives way to some stunning pictures.


# =============================================================================
# Times Table for Set Factor
# =============================================================================

#number of points on the circle
n = 1000

#creating an evenly spaced circle with n points
circle_x = []
circle_y = []
delta = 2*np.pi/n

for i in range(n):
    theta = i*delta
    circle_y.append(np.sin(theta))
    circle_x.append(-np.cos(theta))

#Applying the factor t
t = 21
line_segments = []
for i in range(n):
    j = int(round(t*i)%n)
    line_segments.append(([circle_x[i],circle_x[j]],
                          [circle_y[i],circle_y[j]]))

#Plotting

fig = plt.figure(figsize=(10,10))
plt.axis('off') 
plt.title(t)
plt.scatter(circle_x,circle_y)
for connection in line_segments:
    plt.plot(connection[0], connection[1], alpha = 0.6)
plt.show()

# =============================================================================
# Animation over set values
# =============================================================================

#Circle for animation
circle_x = []
circle_y = []

n = 1000

delta = 2*np.pi/n

writer  = w(fps=5)

for i in range(n):
    theta = i*delta
    circle_y.append(np.sin(theta))
    circle_x.append(-np.cos(theta))
    

#Figure set up
fig = plt.figure(figsize=(10,10))
plt.axis('off') 

#values for animation
l = np.linspace(1, 100, 1000)
for i in range(len(l)):
    l[i] = round(l[i],1)

with writer.saving(fig, 'times_tables.gif', 100):
        
    for t in l:
        plt.axis('off') 
        line_segments = []
        for i in range(n):
            j = int(round(t*i)%n)
            line_segments.append(([circle_x[i],circle_x[j]],
                                  [circle_y[i],circle_y[j]]))
        
        plt.title(t)
        plt.scatter(circle_x,circle_y)
        for connection in line_segments:
            plt.plot(connection[0], connection[1], alpha = 0.6)
        
        print(t)
        
        writer.grab_frame()
        plt.clf()
        










