# Ted Toporkov
# 2024-09-25
# randomseqint.py - generate n random ints between [0..m-1]

import sys
import stdio
import random

m = int(sys.argv[1]) # up to this value int, exclusive
n = int(sys.argv[2]) # total number of ints to generate

count = 0
while count < n:
    stdio.write(random.randint(0, m-1))
    stdio.write(' ')
    count += 1