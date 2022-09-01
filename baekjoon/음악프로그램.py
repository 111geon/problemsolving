import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    dependency = [0 for _ in range(n+1)]
    for _ in range(m):
        singers = list(map(int, input().split()))[1:]
        for i in range(len(singers)-1):
            graph[singers[i]].append(singers[i+1])
            dependency[singers[i+1]] += 1
    
    stack = []
    for i in range(1, n+1):
        if dependency[i] == 0: stack.append(i)

    ans = []
    while stack:
        curr = stack.pop()
        ans.append(curr)
        for nexthop in graph[curr]:
            dependency[nexthop] -= 1
            if dependency[nexthop] == 0:
                stack.append(nexthop)

    if len(ans) == n: 
        for a in ans: print(a)
    else: 
        print(0)    

main()

"""
- 위상정렬
- 순서를 단방향 그래프로 표현하고 노드가 가지고 있는 의존성의 개수를 담는 dependency 배열을 활용
- 스택에 의존성이 0인 노드들을 모두 담는다
- 해당 노드들을 스택에서 꺼내어 방문한다.
    - ans에 추가
    - 해당 노드 이후에 갈 수 있는 노드들의 의존성 개수 1 감소
    - 감소 후 의존성이 0이라면 스택에 추가
- 스택을 다 비운 결과 최종 ans의 개수가 n이라면 모든 노드가 방문됨
    - n이 아닌 경우 모든 노드를 방문하지 못했기 때문에 0 출력
"""
