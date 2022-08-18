import sys
import collections

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, n+1):
        graph[i].sort()

    start, end = map(int, input().split())
    visited_global = [False for _ in range(n+1)]
    ans = find_path_length(n, graph, start, end, visited_global)
    ans += find_path_length(n, graph, end, start, visited_global)
    print(ans)

def find_path_length(n, graph, start, end, visited_global):
    visited = [False for _ in range(n+1)]
    q = collections.deque([(start, [])])
    while q:
        curr, path = q.pop()
        if curr == end:
            for node in path: visited_global[node] = True
            return len(path)

        for nexthop in graph[curr]:
            if not visited[nexthop] and not visited_global[nexthop]:
                visited[nexthop] = True
                q.appendleft((nexthop, path + [nexthop]))

main()

"""
- BFS 탐색을 할 때 큐에는 어떤 노드와 그 노드에 도달하기까지의 경로가 담긴다.
- 목표 노드에 도달하면 쌓아온 경로를 바탕으로 visited_global에 반영한다. 이리하여 시작점에서
  끝점으로 갈 때 거친 노드는 다시 방문하지 않도록 한다.
"""
