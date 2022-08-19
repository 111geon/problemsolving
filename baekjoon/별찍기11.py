import sys
import math

input = sys.stdin.readline

def main():
    n = int(input())
    k = int(math.log2(n // 3))
    m = 6 * 2 ** k - 1

    canvas = [[' ' for _ in range(m)] for _ in range(n)]
    paint(canvas, 0, (m-1)//2, n, m)
    for row in canvas:
        print("".join(row))

def paint(canvas, x, y, n, m):
    if n == 3:
        for i in range(3):
            canvas[x+i][y-i] = canvas[x+i][y+i] = canvas[x+2][y-1+i] = '*'
        return
    paint(canvas, x, y, n//2, (m-1)//2)
    paint(canvas, x+n//2, y-(m+1)//4, n//2, (m-1)//2)
    paint(canvas, x+n//2, y+(m+1)//4, n//2, (m-1)//2)

main()
