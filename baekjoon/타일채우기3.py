import sys; input = sys.stdin.readline

def main():
    n = int(input())
    if n == 1: return print(2)
    dp = [0 for _ in range(n+1)]
    dpsum = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 7
    dpsum[0] = 1
    for i in range(3, n+1):
        dp[i] = (2 * dp[i-1] + 3 * dp[i-2] + 2 * dpsum[i-3]) % 1000000007
        dpsum[i-2] = (dpsum[i-3] + dp[i-2]) % 1000000007
    print(dp[n])

main()

"""
D[i] = 3 * D[i-2] + 2 * D[i-1] + 2 * (D[i-3] + D[i-4] + ... + D[0])
"""
