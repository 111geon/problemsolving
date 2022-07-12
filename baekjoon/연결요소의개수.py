import sys; input = sys.stdin.readline

def main():
    graph = get_input()
    print(solution(graph))

def get_input():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n+1)}

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def solution(graph):
    answer = 0
    visited = [0 for _ in range(len(graph)+1)]
    stack = []
    for curr in graph.keys():
        if visited[curr]: continue
        answer += 1
        visited[curr] = 1
        stack.append(curr)

        while stack:
            for next_node in graph[stack.pop()]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    stack.append(next_node)

    return answer

main()