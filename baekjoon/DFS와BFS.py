import sys

sysinput = sys.stdin.readline

def main():
    n, m, start = map(int, sysinput().split())
    edges = build_edges(n, m)
    print(" ".join(map(str, dfs(n, edges, start))))
    print(" ".join(map(str, bfs(n, edges, start))))

def build_edges(n, m):
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sysinput().split())
        edges[a].append(b)
        edges[b].append(a)

    for e in edges:
        e.sort(reverse=True)

    return edges

def dfs(n, edges, start):
    path = []
    v = [False for _ in range(n+1)]
    stack = [start]
    
    while stack:
        popped_node = stack.pop()
        if not v[popped_node]:
            path.append(popped_node)
            stack += edges[popped_node]
            v[popped_node] = True

    return path

def bfs(n, edges, start):
    path = [start]
    v = [False for _ in range(n+1)]
    v[start] = True
    queue = [start]

    while queue:
        popped_node = queue.pop()
        for next_node in reversed(edges[popped_node]):
            if not v[next_node]:
                queue = [next_node] + queue
                path.append(next_node)
                v[next_node] = True

    return path

main()
