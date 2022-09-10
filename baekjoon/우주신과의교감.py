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
