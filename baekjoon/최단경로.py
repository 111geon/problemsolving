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
if costs[curr] + nextcost <= costs[nexthop]: 의 경우 시간 초과가 발생하였음
"""
