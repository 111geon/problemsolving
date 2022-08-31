import sys; input = sys.stdin.readline
import heapq

def main():
    v, e = map(int, input().split())
    s = int(input())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    costs = [sys.maxsize for _ in range(v+1)]
    costs[s] = 0
    q = [(costs[s], s)]

    while q:
        curr = heapq.heappop(q)[1]
        for nexthop, nextcost in graph[curr]:
            if costs[curr] + nextcost < costs[nexthop]:
                costs[nexthop] = costs[curr] + nextcost
                heapq.heappush(q, (costs[nexthop], nexthop))

    for i in range(1, v+1):
        print(costs[i] if costs[i] != sys.maxsize else 'INF')

main()

"""
- 인접리스트로 그래프를 만든다. (단방향)
- costs 배열은 노드 s로 부터 index에 해당하는 노드까지 가는데 필요한 비용이다.
  초기에는 모든 값을 무한으로 넣어놓고 s에서 s로 가는 비용을 0으로 수정한다.
- q에서는 최소 cost에 해당하는 노드를 pop할 수 있도록 한다.
- q를 모두 소진할 때까지 현재 방문하는 노드 curr를 힙q에서 꺼낸다.
- root로 시작하여 curr를 거쳐 nexthop 노드로 가는 경로가 업데이트 될 수 있다면 업데이트한다.
  업데이트한 노드에 대해 다음에 방문할 수 있도록 힙q에 추가한다.
- 이때 graph에서 cost가 0인 간선은 존재할 수 없기 때문에 cost 업데이트 조건만으로도 방문한 노드를 다시 방문하지 않을 수 있다.
    - if costs[curr] + nextcost <= costs[nexthop] 의 경우 시간 초과가 발생하였음
"""
