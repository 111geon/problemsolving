import sys

def main():
    n = int(sys.stdin.readline())
    memo = {1: 0, 2: 1}
    print(solution(n, memo))

def solution(n, memo):
    if n in memo: return memo[n]
    memo[n] = 1 + min(solution(n//2, memo)+n%2, solution(n//3, memo)+n%3)
    return memo[n]

main()