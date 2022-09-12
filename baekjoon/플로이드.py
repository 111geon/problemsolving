import sys; input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        i, j, c = map(int, input().split())
        graph[i][j] = min(graph[i][j], c)
    
    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j: 
                    graph[i][j] = 0
                    continue
                if i == m or j == m: continue
                graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])
    
    for row in graph[1:]:
        for e in row[1:]:
            if e == sys.maxsize:
                print(0, end=' ')
            else:
                print(e, end=' ')
        print()

main()
