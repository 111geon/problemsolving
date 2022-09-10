import sys; input = sys.stdin.readline
import math

def main():
    n, m = map(int, input().split())
    points = [[0, 0]]
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    
    edges = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            p1, p2 = points[i], points[j]
            edges.append((distance(p1, p2), i, j))
    edges.sort()
    
    group = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if find(group, a) == find(group, b): continue
        union(group, rank, a, b)
        cnt += 1

    print("{:.2f}".format(round(kruskal(n, edges, group, rank, cnt), 2)))

def union(group, rank, node1, node2):
    node1 = find(group, node1)
    node2 = find(group, node2)
    if node1 == node2: return
    if rank[node2] > rank[node1]: node1, node2 = node2, node1
    group[node2] = node1
    if rank[node1] == rank[node2]:
        rank[node1] += 1

def find(group, node):
    if group[node] == node: return node
    group[node] = find(group, group[node])
    return group[node]

def kruskal(n, edges, group, rank, cnt):
    ans = 0
    for d, node1, node2 in edges:
        if cnt == n-1: return ans
        if find(group, node1) == find(group, node2): continue
        union(group, rank, node1, node2)
        cnt += 1
        ans += d

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

main()

"""
- 어차피 모든 간선을 계산하여야하기 때문에 크루스칼 알고리즘이 어울린다고 생각하여 적용.
- 초기에 주어지는 n개의 우주신들의 좌표로부터 모든 edge를 계산한 뒤 정렬한다.
- 그리고 이후에 m개로 주어지는 우주신들간의 연결을 find-union한다.
    - 이때 연결된 신들간의 연결을 cnt로 세어준다.
      총 cnt가 n-1이 되면 크루스칼 로직이 중단되어야 하므로 미리 연결된 연결을 세주는 것.
    - 이때! 중복된 연결 데이터가 제공될 수 있다.
      find root 값이 동일하다면 continue 해버릴 것
- 이후에 크루스칼 알고리즘을 적용해준다.
- 최종 결과를 소수점 2자리로 표현될 수 있도록 round해야한다.
    - 그냥 {:.2f}로 자르면 내림인데 이경우 오답으로 처리됨
"""
