import sys; input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())
    print(solution(a, b, c, {}))

def solution(a, b, c, memo):
    if b < 2:
        return a ** b % c
    if b in memo:
        return memo[b]
    bb = b // 2
    memo[b] = (solution(a, bb, c, memo) * solution(a, b - bb, c, memo)) % c
    return memo[b]

main()
