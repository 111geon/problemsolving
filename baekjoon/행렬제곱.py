import sys; input = sys.stdin.readline

def main():
    n, b = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    for row in solution(n, a, b):
        for e in row:
            print(e % 1000, end=' ')
        print()

def solution(n, a, b):
    if b == 1: return a
    if b % 2 == 1:
        return matmul(n, solution(n, a, b-1), a)
    if b % 2 == 0:
        half = solution(n, a, b//2)
        return matmul(n, half, half)

def matmul(n, a, b):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += a[i][k] * b[k][j]
            ans[i][j] = temp % 1000
    return ans

main()

"""
- 행렬곱을 구현 
- b가 매우 커질수도 있기 때문에 이진분할을 이용
    - b가 홀수 일때는 a의 b-1 제곱과 1 제곱의 행렬 곱을 return
    - 짝수 일때는 a의 b/2 제곱의 행렬을 구하고 그 행렬을 서로 곱
- 행렬곱을 수행할 때마다 최종값에 1000의 나머지로 계산
- 주어지는 a가 [[1000, 1000], [1000, 1000]]일 수도 있음을 염두
"""
