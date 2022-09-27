import sys; input = sys.stdin.readline;

n, m, t = map(int, input().split())
edges = []
group = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

def main():
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()

    cnt = 0
    ans = 0
    for c, a, b in edges:
        if find(a) == find(b): continue
        if cnt == n - 1: break
        ans += c + cnt * t
        union(a, b)
        cnt += 1

    print(ans)

def find(node):
    if group[node] == node: return node
    group[node] = find(group[node])
    return group[node]

def union(a, b):
    a = find(a)
    b = find(b)
    if rank[a] > rank[b]:
        group[b] = a
    elif rank[a] < rank[b]:
        group[a] = b
    else:
        group[b] = a
        rank[a] += 1

main()
