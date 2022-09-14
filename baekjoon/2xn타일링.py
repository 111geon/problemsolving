import sys; input = sys.stdin.readline

def main():
    # main1()
    main2()

def main1():
    n = int(input())
    dp = [0, 1, 2]
    for _ in range(n-2):
        dp.append((dp[-1] + dp[-2]) % 10007)
    print(dp[n])

def main2():
    n = int(input())
    dp = [0, 1, 3]
    for _ in range(n-2):
        dp.append((dp[-1] + 2 * dp[-2]) % 10007)
    print(dp[n])

main()
