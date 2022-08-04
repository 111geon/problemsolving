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
. A B D C
D 0 0 1 1
A 1 1 1 1
B 1 2 2 2
C 1 2 2 3
"""
