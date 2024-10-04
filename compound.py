# Ted Toporkov
# 9/9/2024
# Assignment 1 – Continuously compounded interest

import stdio
import sys
import math

# get cli args and typecast from str to numbers
time = int(sys.argv[1])
principal = int(sys.argv[2])
rate = float(sys.argv[3])

# use pert formula and round result to 2 decimal places
result = round(principal * math.e ** (rate * time), 2)
stdio.writeln(result)