# Ted Toporkov
# 10/31/2024
# recursierpinski.py – This program draws a recursive Sierpinski triangle of order n.

import sys
import stddraw
import time

def draw(n, size, x, y):
    if n == 0: return

    # debug logging
    print(f"Debug: x={x}, y={y}, size={size}, n={n}")

    # plot these coordinages of each triangle's bottom-left starting point
    stddraw.setPenColor(stddraw.RED)
    stddraw.setPenRadius(0.007)
    stddraw.point(x, y)
    stddraw.setPenRadius(0.0)

    # draw the triangle, line by line, 1st line is red, 2nd is blue, 3rd is green
    stddraw.setPenColor(stddraw.RED)
    stddraw.line(x, y, x + size / 2, y + size * (3 ** 0.5) / 2)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.line(x + size / 2, y + size * (3 ** 0.5) / 2, x + size, y)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.line(x + size, y, x, y)

    # draw the internal triangles, recursively
    draw(n-1, size/2, x, y)
    draw(n-1, size/2, x + size/2, y)
    draw(n-1, size/2, x + size/4, y + size * (3 ** 0.5) / 4)

def main():
    n = int(sys.argv[1])
    size = 0.9

    # calculate the coordinates of the triangle's bottom-left vertex
    x = 0.5 - size / 2
    y = 0.5 - size * (3 ** 0.5) / 4

    stddraw.setPenRadius(0.0)
    draw(n, size, x, y)
    stddraw.show()

if __name__ == "__main__":
    main()