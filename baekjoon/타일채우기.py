import sys; input = sys.stdin.readline

def main():
    n = int(input())
    dp = [1, 0, 3]
    for i in range(3, n+1):
        if i % 2 == 1: 
            dp.append(0)
            continue
        temp = 3 * dp[i-2]
        for j in range(4, i+1, 2):
            temp += 2 * dp[i-j]
        dp.append(temp)
    print(dp[n])

main()
