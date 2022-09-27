import sys; input = sys.stdin.readline;
import heapq

def main():
    INF = sys.maxsize
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    dist = [[INF for _ in range(v+1)] for _ in range(v+1)]
    q = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        dist[a][b] = c
        heapq.heappush(q, (c, a, b))

    while q:
        c, a, b = heapq.heappop(q)
        if a == b: 
            print(c)
            return
        for nc, nb in graph[b]:
            if c + nc > dist[a][nb]: continue
            dist[a][nb] = c + nc
            heapq.heappush(q, (c + nc, a, nb))
    
    print(-1)
    

    # graph = [[INF for _ in range(v+1)] for _ in range(v+1)]

    # # for _ in range(e):
    # #     a, b, c = map(int, input().split())
    # #     graph[a][b] = c
    
    # # for m in range(1, v+1):
    # #     for i in range(1, v+1):
    # #         for j in range(1, v+1):
    # #             if i == m or j == m: continue
    # #             if graph[i][j] > graph[i][m] + graph[m][j]:
    # #                 graph[i][j] = graph[i][m] + graph[m][j]

    # # min_cycle = INF
    # # for i in range(1, v+1):
    # #     if graph[i][i] < min_cycle:
    # #         min_cycle = graph[i][i]

    # # if min_cycle == INF: print(-1)
    # # else: print(min_cycle)

main()

"""
- 다익스트라 응용
- 사이클의 시작점이 어디가 될지 모르기 때문에 최소거리를 저장하는 배열이 2차원
- 다음에 볼 노드 및 간선을 넣는 heap에는 다음 노드 뿐만 아니라 시작점의 노드도 같이 저장
    - 태초 시작점의 노드는 힙 안에 있는 동안 계속 유지가 된다.
    - 힙 안에 있는 간선들에 대해 다익스트라 알고리즘을 적용.
    - 힙에서 꺼낸 시작점의 노드와 다음 방문할 노드가 같으면 사이클이 생성된 것.

- 플로이드워셜
- 처음 graph를 만들때 graph[i][i]를 0으로 만들면 안된다.
- 플로이드워셜 알고리즘으로 graph를 업데이트 하면 graph[i][i]들이 사이클이다.
"""
