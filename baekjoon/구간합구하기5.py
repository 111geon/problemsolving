import sys; input = sys.stdin.readline
from itertools import accumulate
from operator import add

n, m = map(int, input().split())

sums = [[0 for _ in range(n+1)]]

for i in range(1, n+1):
    sums.append(list(map(add, [0] + list(accumulate(map(int, input().split()))), sums[i-1])))

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1])
