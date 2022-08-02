import sys; input = sys.stdin.readline

def main():
    n = int(input())
    dp = [[0, 0]]
    for i in range(1, n+1):
        row = list(map(int, input().split()))
        dp.append([0] + [max(dp[i-1][j-1], dp[i-1][j]) + row[j-1] for j in range(1, i+1)] + [0])
    print(max(dp[-1]))

main()
