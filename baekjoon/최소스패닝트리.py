import sys; input = sys.stdin.readline
import heapq

def main():
    v, e = map(int, input().split())
    edges = []
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(prim(v, graph))
    print(kruskal(v, edges))

def prim(v, graph):
    visited = [False for _ in range(v+1)]
    q = [(0, 1)]
    ans = 0
    while q:
        cost, curr = heapq.heappop(q)
        if visited[curr]: continue
        visited[curr] = True
        ans += cost
        for nexthop, nextcost in graph[curr]:
            heapq.heappush(q, (nextcost, nexthop))
    return ans

def kruskal(v, edges):
    edges.sort()

    group = [i for i in range(v+1)]
    rank = [0 for _ in range(v+1)]

    cnt = v - 1
    ans = 0
    for cost, a, b in edges:
        if find(group, a) == find(group, b): continue
        if cnt == 0: break 
        union(group, rank, a, b)
        cnt -= 1
        ans += cost
    
    return ans

def find(group, node):
    if group[node] == node: return node
    group[node] = find(group, group[node])
    return group[node]

def union(group, rank, a, b):
    a = find(group, a)
    b = find(group, b)
    if rank[a] < rank[b]: a, b = b, a
    group[b] = a
    rank[a] += 1

if __name__=="__main__":
    main()

"""
- 크루스칼 알고리즘 O(ElogE) -> 정렬이라 빠름
- edges를 비용을 기준으로 정렬한다.
- 각 노드들은 자기 자신을 번호로 하는 그룹을 갖는다.
    - 그룹은 해당 그룹을 표현하는 트리의 최상단 노드로 대표된다.
    - 각 그룹은 크기를 나타내는 rank를 갖는다.
- v-1개의 간선을 연결할 때 까지 순회문을 돈다.
- a가 속한 그룹과 b가 속한 그룹이 다를 때만 a와 b를 연결해준다.
    - 각 노드가 속한 그룹을 찾아가는 find 과정이 필요하다.
    - 자신이 속한 그룹의 최상단 노드를 찾아가는 과정이 find 과정이다.
    - 그룹 트리는 합쳐지면서 계속 변화하기 때문에 find를 하며 올라가는 과정 중 거치는 노드들의 group을 업데이트 해준다.
- 두 노드를 연결해줄 때 각 노드가 속한 두 개의 그룹을 합쳐주는 union 과정이 필요하다.
    - 더 작은 트리의 최상단 노드가 더 큰 트리의 최상단 노드에 아래로 오게 한다.
    - 더 큰 트리의 크기를 올려준다.
"""

"""
- 프림 알고리즘 O(ElogV) -> 크루스칼보다 느렸음 -> O(VlogV + ElogV)이기 때문에?
- 무방향 graph를 생성
- visited 배열과 queue를 이용하여 BFS 탐색을 한다.
    - queue로 heap을 사용한다는 점에서 dijkstra와 유사하다.
- 큐가 빌 때까지 아래 반복
    - 큐에서 다음 방문할 노드를 꺼내고 해당 노드가 이미 방문되지 않은 노드라면 연결한다.
        - visited 업데이트
        - 비용 총합 업데이트
    - 다음에 방문할 노드들을 큐에 넣는다.
"""
