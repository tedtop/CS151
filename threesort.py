import stdio
import sys

# Read three integers from command line, sort them, and write them to STDIO
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a > b:
    a, b = b, a # Swap a and b
if a > c:
    a, c = c, a # Swap a and c
if b > c:
    b, c = c, b # Swap b and c

stdio.writeln(a)
stdio.writeln(b)
stdio.writeln(c)