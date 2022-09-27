import sys; input = sys.stdin.readline;

def main():
    n = int(input())
    time = [0 for _ in range(n+1)]
    dpnd = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        data = list(reversed(list(map(int, input().split()))))
        time[i] = data.pop()
        while data[-1] != -1:
            graph[data.pop()].append(i)
            dpnd[i] += 1
    
    s = []
    for i in range(1, n+1):
        if dpnd[i] == 0: s.append(i)
    
    dp = time[:]
    while s:
        curr = s.pop()
        for nexthop in graph[curr]:
            dp[nexthop] = max(dp[nexthop], time[nexthop] + dp[curr])
            dpnd[nexthop] -= 1
            if dpnd[nexthop] == 0: s.append(nexthop)
    
    for i in range(1, n+1):
        print(dp[i])

main()

"""
- 위상정렬 + DP
    - 위상정렬: dependency 배열, graph 배열, stack이 필요
    - DP: time 배열, dp 배열이 필요
- 위상정렬 알고리즘을 진행하면서, dp[]에 여러 dependency 중 최대값으로 시간 적용 필요
"""
