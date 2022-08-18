import sys
from collections import deque

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    map_ = []
    for _ in range(n):
        map_.append(input())

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    ans = -1
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        x, y, wall_break = q.pop()
        if x == n - 1 and y == m - 1:
            ans = visited[x][y][wall_break]
            break
        
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            if map_[nx][ny] == '1' and wall_break == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.appendleft((nx, ny, 1))

            if map_[nx][ny] == '0' and not visited[nx][ny][wall_break]:
                visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                q.appendleft((nx, ny, wall_break))

    print(ans)

main()

"""
- 큐에는 node의 x와 y에 대한 정보 뿐만 아니라 현재까지 벽을 부쉈는지에 대한 정보도 저장된다.
- visited는 벽을 안부쉈을 때의 x,y 평면만 있을 뿐 아니라 벽을 부쉈을 때의 xy 평면도 있기 
  때문에 3차원 배열이 되어야한다. 이 배열 안에는 현재까지 거쳐온 노드의 수가 저장된다.
- 시작점에서부터 BFS로 탐색을 수행한다. 탐색 중 목표 노드에 도달하면 종료.
"""
