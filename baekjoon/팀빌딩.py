import sys; input = sys.stdin.readline 

def main():
    n = int(input())
    x = list(map(int, input().split()))
    
    ans = 0
    l, r = 0, n-1
    while l < r:
        ans = max(ans, min(x[l], x[r]) * (r-l-1))
        if x[l] < x[r]: l += 1
        else: r -= 1
    
    print(ans)

main()

"""
- 투 포인터
- 최대의 ans를 찾기 위한 조건
    - l과 r 사이의 사람이 최대한 많거나 - (1)
    - min(x[l], x[r])이 최대한 크다 - (2)
- (2) 조건에 의해 x[l]과 x[r]을 비교하여 더 작은쪽의 포인터를 이동
"""
