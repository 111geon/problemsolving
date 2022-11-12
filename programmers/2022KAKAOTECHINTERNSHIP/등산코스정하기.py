import heapq

MAX_INT = (1 << 63) - 1

def solution(n, paths, gates, summits):
    s_set = set(summits)
    
    G = [[] for _ in range(n+1)]
    for a, b, c in paths:
        G[a].append((b, c))
        G[b].append((a, c))

    v = [False for _ in range(n+1)]
    q = []
    for g in gates:
        for b, c in G[g]:
            heapq.heappush(q, (c, g, b))
        v[g] = True

    ans = [MAX_INT, MAX_INT]
    intensity = 0
    
    while q:
        c, a, b = heapq.heappop(q)
        if v[b]: continue
        
        if a in s_set: continue
        if c > intensity: intensity = c
        if intensity > ans[1]: break
        if b in s_set and b < ans[0]: ans = [b, intensity]
        
        v[b] = True
        for bb, cc in G[b]:
            if v[bb]: continue
            heapq.heappush(q, (cc, b, bb))
    
    return ans

"""
- BFS, prim
- gates에서 시작하는 경로를 모두 힙에 넣고 summit이 나올 때 까지 프림 알고리즘 진행
- summit을 거쳐서 가는 모든 경로는 무효하므로 현재 경로의 시작점이 summit이라면 continue
- intensity는 heap의 특성을 이용하여 단조 증가한다. 이 값이 ans를 넘어가면 pruning.
"""
