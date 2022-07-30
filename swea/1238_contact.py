import collections

def main():
    for t in range(1, 11):
        n, start = map(int, input().split())
        graph = collections.defaultdict(list)
        connection_data = list(map(int, input().split()))
        for i in range(0, n, 2):
            graph[connection_data[i]].append(connection_data[i+1])
        print("#" + str(t), solution(graph, start))

def solution(graph, start):
    visited = set()
    q = []
    q.append(start)
    visited.add(start)

    while True:
        tmp = []
        for curr in q:
            for next_node in graph[curr]:
                if next_node not in visited:
                    visited.add(next_node)
                    tmp.append(next_node)
        if not tmp:
            break
        q = tmp

    return str(max(q))

main()
