import sys; input = sys.stdin.readline
import heapq

def main():
    n, m, r = map(int, input().split())
    t = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))

    ans = 0
    for i in range(1, n+1):
        ans = max(ans, search(n, graph, m, t, i))
    
    print(ans)

def search(n, graph, m, t, root):
    ans = 0
    visited = [False for _ in range(n+1)]
    costs = [sys.maxsize for _ in range(n+1)]
    costs[root] = 0
    q = [(0, root)]
    
    while q:
        curr = heapq.heappop(q)[1]
        if visited[curr]: continue
        if costs[curr] > m: break
        visited[curr] = True
        ans += t[curr]

        for nexthop, nextcost in graph[curr]:
            if costs[nexthop] > costs[curr] + nextcost:
                costs[nexthop] = costs[curr] + nextcost
                heapq.heappush(q, (costs[nexthop], nexthop))

    return ans

main()

"""
- search 함수는 root 노드로부터 최대 m까지 떨어진 노드들의 t를 더한 값을 반환하는 함수다.
- 이미 파밍한 노드는 다시 파밍하지 않도록 visited를 만들어준다.
- costs는 root로 부터 index에 해당하는 노드까지 갈 때 필요한 비용이다.
- q에는 비용이 앞으로 나와서 최소 비용이 heappop 될 수 있도록 넣어준다.
- 이미 방문한 노드가 힙에서 pop되면 그냥 지나간다.
- 방문할 노드들은 비용이 작은 순으로 순서대로 나온다.
  따라서 힙에서 pop한 노드의 비용이 m을 넘어버린다면 이후 노드들도 다 m을 넘을 것이다. -> break
- 노드를 방문함과 동시에 ans에 파밍한 아이템 수를 추가해준다.
- graph를 확인하여 다음 방문할 수 있는 노드들을 업데이트한다.
"""
