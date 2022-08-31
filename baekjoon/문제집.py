import sys; input = sys.stdin.readline
import heapq as hq

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dependency = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        dependency[b] += 1

    q = []
    for i in range(1, n+1):
        if dependency[i] == 0: hq.heappush(q, i)
    ans = []
    while q:
        curr = hq.heappop(q)
        ans.append(curr)
        for nexthop in graph[curr]:
            dependency[nexthop] -= 1
            if dependency[nexthop] == 0: hq.heappush(q, nexthop)

    print(" ".join(map(str, ans)))

main()

"""
- 위상정렬
- 처음에는 dependencies[b]에 a가 있다면 a를 우선 확인한다! 라고 접근했었다.
  이경우 3 -> 1, 2 -> 4 -> 1 과 같은 경우일 때 참으로 곤란함
- 대신 단방향 그래프를 평소와 같이 정의하고 dependency 배열을 활용
  이 배열은 인덱스에 해당하는 노드가 가지고 있는 의존성의 개수를 의미한다.
- 큐에는 의존성이 0인 노드들이 담긴다! 최소 노드를 먼저 방문하고 싶기 때문에 힙을 이용한다.
- 초기 힙에는 의존성이 0인 노드들이 쭉 담긴다.
- 힙에서 최소 노드를 꺼내가며 스택에 쌓고 해당 노드에 의존하는 노드들의 의존성 개수를 줄여준다.
  만약 의존성이 준 노드의 의존성이 0이 되어버렸다면 해당 노드는 큐에 들어올 수 있게 된다.
  
"""
