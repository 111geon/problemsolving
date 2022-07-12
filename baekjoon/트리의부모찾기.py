import sys; input = sys.stdin.readline
from collections import defaultdict
from collections import deque

n = int(input())

graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

root = 1
level = {root: 1}
visited = set([root])
queue = deque([root])
while queue:
    curr_node = queue.pop()
    for next_node in graph[curr_node]:
        if next_node not in visited:
            level[next_node] = level[curr_node] + 1
            visited.add(next_node)
            queue.appendleft(next_node)

for node in range(2, n+1):
    for connected in graph[node]:
        if level[connected] == level[node] - 1:
            print(connected)
            break
