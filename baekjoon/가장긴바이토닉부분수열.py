import sys; input = sys.stdin.readline 

def main():
    n = int(input())
    ls = list(map(int, input().split()))

    dp1 = [1 for _ in range(n)]
    dp2 = [1 for _ in range(n)]
    lower_bound_lis(n, ls, dp1)
    lower_bound_lis(n, list(reversed(ls)), dp2)

    ans = 0
    for i in range(n): ans = max(ans, dp1[i] + dp2[n-i-1])
    print(ans-1)

def lower_bound_lis(n, ls, dp):
    lb = [ls[0]]
    for i in range(1, n):
        if lb[-1] < ls[i]:
            lb.append(ls[i])
            dp[i] = len(lb)
            continue

        l, r = 0, len(lb) - 1
        while l < r:
            mid = (l + r) // 2
            if lb[mid] == ls[i]:
                l = mid
                break
            if lb[mid] < ls[i]:
                l = mid + 1
            else:
                r = mid
        lb[l] = ls[i]
        dp[i] = len(lb)

main()

"""
- 순방향 LIS와 역방향 LIS 리스트를 생성
    - 순방향은 증가하는 반쪽, 역방향은 감소하는 반쪽을 나타낸다
- 둘의 합이 가장 큰 지점이 꼭대기 지점이다.
- LIS 생성은 lower bound와 이진탐색을 이용
"""
