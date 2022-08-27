import sys; input = sys.stdin.readline
import heapq

def main():
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))  # (node, cost)
        graph[b].append((a, cost))
    
    u, v = map(int, input().split())
    route_1u = dijkstra(n, graph, 1, u)
    route_1v = dijkstra(n, graph, 1, v)
    route_un = dijkstra(n, graph, u, n)
    route_vn = dijkstra(n, graph, v, n)
    route_uv = dijkstra(n, graph, u, v)
    if route_uv == -1:
        print(-1)
    elif route_1u == -1 or route_vn == -1:
        print(-1)
    else:
        print(route_uv + min(route_1u + route_vn, route_1v + route_un))

def dijkstra(n, graph, a, b):
    cost = [sys.maxsize for _ in range(n+1)]
    cost[a] = 0

    q = [(0, a)]  # (cost, node)
    while q:
        curr = heapq.heappop(q)[1];
        if curr == b: return cost[b]
        for nexthop, ncost in graph[curr]:
            if cost[curr] + ncost <= cost[nexthop]:
                cost[nexthop] = cost[curr] + ncost
                heapq.heappush(q, (cost[nexthop], nexthop))
    
    return -1

main()

"""
- 다익스트라 알고리즘
- 1 -> u -> v -> n 또는 1 -> v -> u -> n 두 경로가 있다. 각각 비용을 구해서 비교하자.
- 이 그래프의 경우 cost가 0인 경우가 없으므로, 비용 갱신 시 이미 방문한 노드는 갱신될 일이
  없어 visited 배열 또한 필요가 없다.
- 출발노드와 도착노드가 단절되어 있는 경우 q가 모두 소진되어도 cost를 반환할 수 없다.
- uv가 끊어져 있거나, 1 또는 n이 동떨어져있는 경우 전체 경로는 발생할 수 없다.
"""
