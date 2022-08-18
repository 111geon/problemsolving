import sys
import collections

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n, m = map(int, input().split())
    graph = collections.defaultdict(list)
    has_parent = [False for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)
        has_parent[a] = True
    
    visited_global = [False for _ in range(n+1)]
    
    scores = [0] + [1 for _ in range(n)]
    for node in range(1, n+1):
        if has_parent[node]: continue
        scores[node] = hack(graph, node, n, visited_global)

    sccs = []
    for node in range(1, n+1):
        if not visited_global[node]:
            sccs.append(node)

    for node in sccs: 
        scores[node] = hack(graph, node, n, visited_global)
    
    answer = []
    max_score = max(scores)
    for node in range(1, n+1):
        if scores[node] == max_score: answer.append(node)

    print(" ".join(map(str, answer)))

def hack(graph, start, n, visited_global):
    ans = 1
    q = collections.deque([start])
    visited = [False for _ in range(n+1)]
    visited[start] = True
    visited_global[start] = True

    while q:
        for nexthop in graph[q.pop()]:
            if not visited[nexthop]:
                ans += 1
                visited[nexthop] = True
                q.appendleft(nexthop)
                visited_global[nexthop] = True

    return ans

main()

"""
- A가 B를 신뢰한다는 것은 B를 해킹하면 A를 해킹할 수 있다는 것으로 B -> A 그래프로 표현 가능
- 모든 노드들을 돌며 각각에 대해 DFS 또는 BFS를 통해 감염 가능한 노드 수를 구해야 한다.
    - A -> B, A -> C, B -> C 구조 때문에 DP로 저장해두는 것을 사용하는 것은 불가하다.
    - 모든 노드를 도는 것이 시간이 오래 걸리기 때문에 시간을 줄일 수 있도록 해야한다.
- 전체 그래프가 어찌되었건 A -> B 가 있다면 B보다는 A가 점수가 더 높을것, B는 순회 대상에서 제외
    - 이때 A -> B -> C -> A, A -> D 와 같이 순환하는 구조가 있다면 A는 부모가 있지만
      최대 점수를 가질 수도 있는 존재다.
- 순환하는 SCC 요소들도 순회해주기 위해 지금까지 한번도 방문되지 못한 노드가 있다면 이 노드들을
  순회해준다.
"""
