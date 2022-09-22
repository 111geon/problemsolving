import sys; input = sys.stdin.readline

def main():
    tc = int(input())

    dp = [[0 for _ in range(11)] for _ in range(2001)]
    for i in range(1, 2001):
        dp[i][1] = i

    for i in range(2, 11):
        for j in range(1, 2001):
            dp[j][i] = dp[j-1][i] + dp[j//2][i-1]

    for _ in range(tc):
        n, m = map(int, input().split())
        print(dp[m][n])

main()
