import sys

input = sys.stdin.readline

def main():
    n, s, m = map(int, input().split())
    dv = list(map(int, input().split()))

    memo = [set() for _ in range(n+1)]
    memo[0].add(s)
    for i in range(1, n+1):
        for v in memo[i-1]:
            for nv in (v - dv[i-1], v + dv[i-1]):
                if 0 <= nv <= m:
                    memo[i].add(nv)
    
    if (memo[-1]): print(max(memo[-1]))
    else: print(-1)

main()

"""
- memo[i]는 memo[i-1]로 부터 나온 볼륨들을 기준으로 계산한 nv(주어진 볼륨 차를 더하거나 뺀 값)
  중 조건에 맞는 값들을 넣은 set이다.
"""
