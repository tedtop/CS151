# Ted Toporkov
# 10/4/2024
# circle.py - draws a circle

import sys
import math
import stdio
import stddraw
import stdarray
import random

n = 36
p = 0.01

# Check if args are provided
print(len(sys.argv))
if not len(sys.argv) > 2:
    print("Usage: python circle.py <number of points to draw around cirle> <probability of connecting them>")
    sys.exit(1)

n = int(sys.argv[1]) # number of points to plot around a circle
p = float(sys.argv[2]) # probability of connecting the points

radius = 50 # 1. set a radius for the cirle
angle = 360 / n # 2. 360° degrees devide by how many how many points around the circle

# initialize the canvas
stddraw.setXscale(-radius - 5, radius + 5)
stddraw.setYscale(-radius - 5, radius + 5)
stddraw.setPenRadius(0.005)
stddraw.setPenColor(stddraw.BLACK)

# initialize an array of coords where the key is x and the value is y with size n
coords = stdarray.create1D(n, 0.0)
for i in range(n):
    # 𝑥=𝑟cos(𝜃)
    # 𝑦=𝑟sin(𝜃)

    # find the x and y coordinates of the point given the angle and radius as hyponuse
    x = radius * math.cos(math.radians(angle * i))
    y = radius * math.sin(math.radians(angle * i))

    # store the x and y coordinates in the array
    coords[i] = (x, y)

for j in range(len(coords)):
    stddraw.point(coords[j][0], coords[j][1]) # plot each of the n points

    # for each new point, draw a line to each existing point with p probability
    for k in range(len(coords)):

        # generate a random number between 0 and 1
        to_draw_or_not_to_draw = random.random()
        if (to_draw_or_not_to_draw < p):
            # stddraw.line(x0, y0, x1, y1) # draw a line from (x0, y0) to (x1, y1)
            stddraw.line(coords[j][0], coords[j][1], coords[k][0], coords[k][1])

stddraw.show()