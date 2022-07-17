from operator import mul

def main():
    t = int(input())
    for tt in range(1, t+1):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print("#" + str(tt) + " " + solution(n, m, a, b))

def solution(n, m, a, b):
    short = a if n < m else b
    long = a if n > m else b
    
    ans = 0
    for i in range(len(long)-len(short)+1):
        ans = max(ans, sum(map(mul, short, long[i:i+len(short)])))
    
    return str(ans)

main()
