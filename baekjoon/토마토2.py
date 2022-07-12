import sys; input = sys.stdin.readline

def main():
    tomatoes = get_inputs()
    print(solution(tomatoes))
    return

def get_inputs():
    m, n, h = map(int, input().split())
    tomatoes = [[[-1 for _ in range(m+2)] for _ in range(n+2)]]
    for _ in range(h):
        temp = [[-1 for _ in range(m+2)]]
        for _ in range(n):
            temp.append([-1] + list(map(int, input().split())) + [-1])
        temp.append([-1 for _ in range(m+2)])
        tomatoes.append(temp)
    tomatoes.append([[-1 for _ in range(m+2)] for _ in range(n+2)])
    return tomatoes

def solution(tomatoes):
    answer = 0
    unriped = 0
    stack = []

    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for h, level in enumerate(tomatoes):
        for i, row in enumerate(level):
            for j, tomato in enumerate(row):
                if tomato == 0: unriped += 1
                if tomato == 1: stack.append((h, i, j))

    while stack:
        temp = []
        for tomato in stack:
            for i in range(len(dx)):
                nz = tomato[0] + dz[i]
                nx = tomato[1] + dx[i]
                ny = tomato[2] + dy[i]
                if tomatoes[nz][nx][ny] == 0:
                    tomatoes[nz][nx][ny] = 1
                    temp.append((nz, nx, ny))
                    unriped -= 1
        stack = temp
        answer += 1
    
    if unriped != 0: 
        return -1

    return answer-1

main()
