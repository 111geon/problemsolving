import heapq

def main():
    t = int(input())
    for tt in range(1, t+1):
        n = int(input())
        mat = []
        for _ in range(n):
            mat.append(list(map(int, list(input().strip()))))
        print("#" + str(tt), solution(n, mat))
    
def solution(n, mat):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    maxsize = 2**63-1
    for i in range(n):
        mat[i] = [maxsize] + mat[i] + [maxsize]
    padding_m = [[maxsize for _ in range (n+2)]]
    mat = padding_m + mat[:] + padding_m

    visited = [[1 for _ in range(n+2)]]
    for _ in range(n):
        visited.append([1] + [0 for _ in range(n)] + [1])
    visited.append([1 for _ in range(n+2)])

    hq = []
    visited[1][1] = 1
    hq.append((0, 1, 1))

    while True:
        cost, x, y = heapq.heappop(hq)
        if x == n and y == n:
            return str(cost)
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny]: continue
            ncost = cost + mat[nx][ny]
            visited[nx][ny] = 1
            heapq.heappush(hq, (ncost, nx, ny))

main()
