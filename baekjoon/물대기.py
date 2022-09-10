import sys; input = sys.stdin.readline
import heapq

def main():
    n = int(input())
    q = []
    graph = []
    for i in range(n): heapq.heappush(q, (int(input()), i))
    for i in range(n): graph.append(tuple(map(int, input().split())))

    visited = [False for _ in range(n)]
    ans = 0
    while q:
        cost, curr = heapq.heappop(q)
        if visited[curr]: continue
        ans += cost
        visited[curr] = True
        for nexthop in range(n):
            if nexthop == curr or visited[nexthop]: continue
            nextcost = graph[curr][nexthop]
            heapq.heappush(q, (nextcost, nexthop))
    
    print(ans)

main()

"""
- 모든 논에는 물을 대는 방법이 두가지가 있다.
    - 본인 스스로 우물을 파는 것
    - 우물을 판 마을이 포함된 트리에 자신도 포함되는 것.
- 이는 아래와 같이 해석할 수 있다.
    - 우물을 포함하는 트리를 시작하는 것
    - 이미 우물이 포함된 트리를 확장하는 것
    - 이는 프림 알고리즘을 적용하기에 딱이다.
- 우물을 파는 비용과 해당 논의 번호를 힙에 모두 넣는다.
    - 이로써 우물 파는 비용이 다른 논과 연결하는 비용보다 저렴하다면 언제든 우물을 팔 수 있게 되었다.
- 현재 큐에는 모두 우물을 파는 경우만 있기 때문에 최초로 어떤 논이던 우물을 파게 된다.
    - 그 이후 해당 논과 연결된 다른 논들과의 연결을 힙에 넣는다.
    - 그리하여 해당 논의 트리를 확장할지 아니면 새로운 우물이 포함된 트리를 생성할지 힙이 결정하게 한다.
"""
