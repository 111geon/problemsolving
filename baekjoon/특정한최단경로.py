import sys; input = sys.stdin.readline
import heapq

def main():
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    u, v = map(int, input().split())
    route_1u = dijkstra(n, graph, 1, u)
    route_1v = dijkstra(n, graph, 1, v)
    route_un = dijkstra(n, graph, u, n)
    route_vn = dijkstra(n, graph, v, n)
    route_uv = dijkstra(n, graph, u, v)
    # if (route_uv == sys.maxsize)
    print(route_uv + min(route_1u + route_vn, route_1v + route_un))

def dijkstra(n, graph, a, b):
    cost = [sys.maxsize for _ in range(n+1)]
    for e in graph[a]: cost[e[0]] = e[1]
    visited = [False for _ in range(n+1)]
    visited[a] = True
    q = []
    for i in range(1, n+1): heapq.heappush(q, (cost[i], i))
    print(q)


main()
