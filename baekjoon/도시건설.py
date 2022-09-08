import sys; input = sys.stdin.readline 

def main():
    n, m = map(int, input().split())
    total = 0
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        total += c
        edges.append([c, a, b])
    print(solution(n, edges, total))

def solution(n, edges, total):
    edges.sort()
    cnt = 0
    ans = 0
    group = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]
    for c, a, b in edges:
        if cnt == n - 1: break
        if find(group, a) == find(group, b): continue 
        union(group, rank, a, b)
        cnt += 1
        ans += c
    else:
        return -1
    return total - ans

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

main()

"""
- 최소 스패닝 트리와 동일한 문제
- edge를 모두 순회했음에도 불구하고 cnt가 n-1이 되지 못하는 부분 처리.
    - 스패닝 트리가 연결되지 못했음을 의미
"""
