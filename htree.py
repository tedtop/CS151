import sys
import stddraw

def draw(n, size, x, y):
    if n == 0: return
    x0 = x - size/2.0
    x1 = x + size/2.0
    y0 = y - size/2.0
    y1 = y + size/2.0
    stddraw.line(x0, y, x1, y)
    stddraw.line(x0, y0, x0, y1)
    stddraw.line(x1, y0, x1, y1)
    draw(n-1, size/2.0, x0, y0)
    draw(n-1, size/2.0, x0, y1)
    draw(n-1, size/2.0, x1, y0)
    draw(n-1, size/2.0, x1, y1)

n = int(sys.argv[1])
stddraw.setPenRadius(0.0)
draw(n, 0.5, 0.5, 0.5)
stddraw.show()