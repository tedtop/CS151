# Ted Toporkov
# 9/9/2024
# Assignment 2 – Wind chill calculation

import stdio
import sys

t = float(sys.argv[1]) # outside air temp (°F)
v = float(sys.argv[2]) # wind velocity (MPH)

# do wind chill calculation
wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)

stdio.writeln('Temperature = ' + str(t))
stdio.writeln('Wind speed  = ' + str(v))
stdio.writeln('Wind chill  = ' + str(wind_chill))