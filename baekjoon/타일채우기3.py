import sys; input = sys.stdin.readline

def main():
    n = int(input())
    if n == 1: return print(2)
    dp = [[0, 0] for _ in range(n+1)]
    dp[0] = [1, 1]
    dp[1][0] = 2
    dp[2][0] = 7
    for i in range(3, n+1):
        dp[i][0] = (2 * dp[i-1][0] + 3 * dp[i-2][0] + 2 * dp[i-3][1]) % 1000000007
        dp[i-2][1] = (dp[i-3][1] + dp[i-2][0]) % 1000000007
    print(dp[n][0])

main()

"""
D[i] = 3 * D[i-2] + 2 * D[i-1] + 2 * (D[i-3] + D[i-4] + ... + D[0])
"""
