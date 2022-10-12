import sys

def solution(n, s, a, b, fares):
    graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
        
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if start == mid or end == mid: continue
                if graph[start][mid] + graph[mid][end] < graph[start][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
    
    answer = sys.maxsize
    for mid in range(1, n+1):
        answer = min(answer, graph[s][mid] + graph[mid][a] + graph[mid][b])
    
    return answer

"""
- 플로이드 워셜 알고리즘
- 모든 지점 간의 최단 비용을 구한다.
- 모든 지점을 탐색하면서 합승을 어디까지 하는게 가장 적은 비용이 발생하는지 찾는다.
"""
