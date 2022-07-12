import sys; input = sys.stdin.readline

n = int(input())
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
dp3 = [0 for _ in range(n)]
a, b, c = map(int, input().split())
dp1[0] = a
dp2[0] = b
dp3[0] = c
for i in range(1, n):
    a, b, c = map(int, input().split())
    dp1[i] = a + min(dp2[i-1], dp3[i-1])
    dp2[i] = b + min(dp1[i-1], dp3[i-1])
    dp3[i] = c + min(dp1[i-1], dp2[i-1])

print(min(dp1[-1], dp2[-1], dp3[-1]))