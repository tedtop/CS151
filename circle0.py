import stddraw
import random

stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)
stddraw.setPenRadius(0.01)

while True:
    x = -1.0 + 2.0 * random.random()
    y = -1.0 + 2.0 * random.random()
    if x * x + y * y <= 1.0:
        break

stddraw.circle(0,0,1)
stddraw.point(x,y)
stddraw.show()