import sys; sysinput = sys.stdin.readline
import collections

def main():
    n = int(sysinput())
    m = int(sysinput())
    g = collections.defaultdict(list)
    for _ in range(m):
        a, b = map(int, sysinput().split())
        g[a].append(b)
        g[b].append(a)

    answer = 0
    start = 1
    v = [False for _ in range(n+1)]
    v[start] = True
    s = [start]

    while s:
        curr = s.pop()
        for next_node in g[curr]:
            if not v[next_node]:
                answer += 1
                v[next_node] = True
                s.append(next_node)

    print(answer)

main()
