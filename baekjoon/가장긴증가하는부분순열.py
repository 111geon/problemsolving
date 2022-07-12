import sys; input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


# lower bound

b = [a[0]]
for i in range(1, n):
    j = 0
    while j < len(b):
        if a[i] <= b[j]:
            b[j] = a[i]
            break
        j += 1
    else:
        b.append(a[i])

print(len(b))


# dynamic programming

# dp = [1 for _ in range(n)]

# for i in range(1, n):
#     for j in range(i-1, -1, -1):
#         if a[i] > a[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))