# Ted Toporkov
# 2024-09-25
# racecars.py

import stddraw
import random

car_width = 0.04
car_height = 0.02

# Initial positions of the cars
x1 = 0.0
x2 = 0.0

while True:
    stddraw.clear()
    stddraw.rectangle(x1 / 10, 0.33, car_width, car_height)
    stddraw.rectangle(x2 / 10, 0.66, car_width, car_height)

    # Generate random velocities for the cars
    v1 = abs(random.random()) * 0.1
    v2 = abs(random.random()) * 0.1

    # Update the positions of the cars
    x1 += v1
    x2 += v2

    # Check if any car has reached the finish line
    if x1 > 10:
        stddraw.text(0.5, 0.5, "Car 1 wins!")
        stddraw.show()
        break
    elif x2 > 10:
        stddraw.text(0.5, 0.5, "Car 2 wins!")
        stddraw.show()
        break
    else:
        # Write text below each car to indicate its x position
        stddraw.text(0.5, 0.30, "Car 1: x={:.2f}".format(x1))
        stddraw.text(0.5, 0.63, "Car 2: x={:.2f}".format(x1))

    stddraw.show(60)