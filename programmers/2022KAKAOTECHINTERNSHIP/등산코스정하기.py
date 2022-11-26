import heapq

MAX_INT = (1 << 63) - 1

def solution(n, paths, gates, summits):
    summits_set = set(summits)
    
    graph = [[] for _ in range(n+1)]
    for curr, nxt, cost in paths:
        graph[curr].append((nxt, cost))
        graph[nxt].append((curr, cost))

    visited = [False for _ in range(n+1)]
    queue = []
    for gate in gates:
        for nxt, cost in graph[gate]:
            heapq.heappush(queue, (cost, gate, nxt))
        visited[gate] = True

    answer = [MAX_INT, MAX_INT]
    intensity = 0
    
    while queue:
        cost, curr, nxt = heapq.heappop(queue)
        if visited[nxt]: continue
        
        if curr in summits_set: continue
        if cost > intensity: intensity = cost
        if intensity > answer[1]: break
        if nxt in summits_set and nxt < answer[0]: answer = [nxt, intensity]
        
        visited[nxt] = True
        for nxtnxt, nextcost in graph[nxt]:
            if visited[nxtnxt]: continue
            heapq.heappush(queue, (nextcost, nxt, nxtnxt))
    
    return answer

"""
- BFS, prim
- gates에서 시작하는 경로를 모두 힙에 넣고 summit이 나올 때 까지 프림 알고리즘 진행
- summit을 거쳐서 가는 모든 경로는 무효하므로 현재 경로의 시작점이 summit이라면 continue
- intensity는 heap의 특성을 이용하여 단조 증가한다. 이 값이 ans를 넘어가면 pruning.
"""
