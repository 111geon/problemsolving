import sys; input = sys.stdin.readline

def main():
    n = int(input())
    house = [['0'] * (n+1)]
    for _ in range(n):
        house.append(['0'] + input().split())
    
    memo = [[[0, 0, 0] for _ in range(n+1)] for _ in range(n+1)] # [가로, 세로, 대각]
    memo[1][2][0] = 1
    for i in range(1, n+1):
        for j in range(3, n+1):
            if house[i][j] == '1': continue
            if house[i][j-1] == '0':
                memo[i][j][0] = memo[i][j-1][0] + memo[i][j-1][2]
            if house[i-1][j] == '0':
                memo[i][j][1] = memo[i-1][j][1] + memo[i-1][j][2]
            if house[i][j-1] == '0' and house[i-1][j] == '0' and house[i-1][j-1] == '0':
                memo[i][j][2] = memo[i-1][j-1][2] + memo[i-1][j-1][0] + memo[i-1][j-1][1]
    
    print(sum(memo[-1][-1]))

main()
