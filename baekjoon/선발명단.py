import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        power = []
        for _ in range(11):
            power.append(list(map(int, input().split())))
        visited = [False for _ in range(11)]
        print(dfs(power, visited, 0, 0, 0))

def dfs(power, visited, x, total, max_total):
    if x >= 11:
        return max(total, max_total)
    for i in range(11):
        if not visited[i] and power[x][i]:
            visited[i] = True
            total += power[x][i]
            max_total = dfs(power, visited, x+1, total, max_total)
            total -= power[x][i]
            visited[i] = False
    return max_total

main()

"""
- 백트래킹
- 포지션 별로 visited 배열을 만든다.
- 사람(x)를 순회하면서 해당 사람을 배치가능한(방문하지 않았고 score가 0이 아님) 포지션에 배치
- 모든 사람을 배치했을 때(x가 11이상일 때) 최대 점수를 갱신한다.
"""
