import sys
sysinput = sys.stdin.readline

def main():
    n = int(sysinput())
    step = []
    for _ in range(n):
        step.append(int(sysinput()))

    if n == 1: return step[0]
    if n == 2: return step[0] + step[1]
    if n == 3: return max(step[0], step[1])+step[2]

    memo = [step[0], step[0]+step[1], max(step[0], step[1])+step[2]]
    for i in range(3, n):
        memo.append(step[i] + max(memo[i-2], memo[i-3]+step[i-1]))
    
    return memo[n-1]

print(main())
