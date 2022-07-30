def main():
    t = int(input())
    for tt in range(1, t+1):
        n, m = map(int, input().split())
        print("#" + str(tt) + " " + solution(n, m))

def solution(n, m):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        row = list(map(int, input().split()))
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + row[j-1]

    ans = 0
    for i in range(m, n+1):
        for j in range(m, n+1):
            ans = max(ans, dp[i][j] - dp[i-m][j] - dp[i][j-m] + + dp[i-m][j-m])

    return str(ans)    

main()
