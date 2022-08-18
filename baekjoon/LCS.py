import sys
input = sys.stdin.readline

def main():
    a = input().strip()
    b = input().strip()

    memo = [[0 for _ in range(len(b)+1)]]
    for i in range(1, len(a)+1):
        row = [0]
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                row.append(memo[i-1][j-1] + 1)
                continue
            row.append(max(memo[i-1][j], row[j-1]))
        memo.append(row)

    print(memo[-1][-1])

main()

"""
- 2차원 DP로 표현 (편의상 패딩을 추가)
    . A B D C
    D 0 0 1 1
    A 1 1 1 1
    B 1 2 2 2
    C 1 2 2 3
- dp[i][j]는 a[:i+1]와 b[:j+1]의 LCS 길이를 표현한다.
- a[i]와 b[j]가 같다면 dp[i-1][j-1]에서 LCS 길이가 1 증가한 것과 같다.
- a[i]와 b[j]가 같지 않다면, dp[i-1][j]와 dp[i][j-1] 중 더 큰 값으로 채운다.
"""
