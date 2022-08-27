import sys
import heapq

input = sys.stdin.readline

def main():
    n = int(input())   
    graph = [[] for _ in range(n+1)]

    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    a, b = map(int, input().split())
    cost = [sys.maxsize for _ in range(n+1)]
    cost[a] = 0
    visited = [False for _ in range(n+1)]
    q = [(0, a)]

    while q:
        curr = heapq.heappop(q)[1]
        if visited[curr]: continue
        visited[curr] = True
        if curr == b: break
        for nexthop, nextcost in graph[curr]:
            if cost[curr] + nextcost < cost[nexthop]:
                cost[nexthop] = cost[curr] + nextcost
                heapq.heappush(q, (cost[nexthop], nexthop))

    print(cost[b])

main()

"""
- 다익스트라 알고리즘은 시작점 노드를 기준으로 다른 노드들과의 거리를 담는 cost 배열이 필요하다.
  또 이 배열을 갱신할 때마다 cost를 기준으로 정렬한 heap에 추가하여 가장 작은 cost를 갖는 노드를
  찾아낸다.
- 도착노드를 방문할 때까지 loop을 돌린다.
- heap에서 노드들을 꺼내며 가장 비용이 작은 노드를 찾는다
- 해당 노드는 이미 방문되었지만 예전 cost가 q에 남아있는 경우일 수 있다. 방문된 경우 continue.
- 그 노드를 방문하면서 그 노드와 연결된 다른 노드들을 peek하며 cost를 갱신할 수 있는 경우
  갱신을 하고 heap에 갱신한 노드와 비용을 추가한다.
"""
