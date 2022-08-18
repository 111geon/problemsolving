import sys; input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = [a[0]]
    for i in range(1, n):
        j = 0
        while j < len(b):
            if a[i] <= b[j]:
                b[j] = a[i]
                break
            j += 1
        else:
            b.append(a[i])

    print(len(b))

main()

"""
- 수열 B는 현재 시점에서 가장 긴 증가하는 부분 수열을 갱신해 나가는 수열이다.
- 수열 A를 앞에서부터 순회하며 뽑은 값을 들고 수열 B를 본다.
- A의 값이 수열 B 안에 어떤 값보다 작다면 그 A의 값은 해당 B의 값이 있던 자리에 들어간다.
- 만약 A의 값이 B의 어느 자리에도 들어가지 못했다면 해당 A의 값은 B의 모든 값보다 크다는 뜻이기
  때문에 해당 A 값은 B의 맨 뒤에 추가된다.
- 해당 방식으로 진행하면 B의 크기는 현재까지 나온 가장 긴 증가하는 부분 수열의 크기를 나타낸다.
"""

# dp = [1 for _ in range(n)]

# for i in range(1, n):
#     for j in range(i-1, -1, -1):
#         if a[i] > a[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))
