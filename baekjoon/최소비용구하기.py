import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    n = int(input())   
    graph = collections.defaultdict(list)

    for _ in range(int(input())):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))

    a, b = map(int, input().split())
    dist = [sys.maxsize for _ in range(n+1)]
    dist[a] = 0
    visited = set()
    q = [(0, a)]

    while b not in visited:
        while q:
            next_node = heapq.heappop(q)[1]
            if next_node not in visited: break 
        visited.add(next_node)

        for cand, w in graph[next_node]:
            dist[cand] = min(dist[cand], dist[next_node] + w)
            heapq.heappush(q, (dist[cand], cand))

    print(dist[b])

main()

"""
- 다익스트라 알고리즘은 시작점 노드를 기준으로 다른 노드들과의 거리를 담는 distance 배열이
  필요하다. 또 이 배열을 갱신할 때마다 cost를 기준으로 정렬한 heap에 추가하여 가장 작은
  distance를 갖는 노드를 찾아낸다.
- 도착노드를 방문할 때까지 loop을 돌린다.
- heap에서 노드들을 꺼내며 아직 방문하지 않은 노드 중에 가장 dist가 작은 노드를 찾는다
- 그 노드를 방문하면서 그 노드와 연결된 다른 노드들을 peek하며 distance를 갱신한다.
    dist[cand] = min(dist[cand], dist[next_node] + w)
- 이때, heap에 갱신되는 노드들을 추가해주어야 한다.
"""
