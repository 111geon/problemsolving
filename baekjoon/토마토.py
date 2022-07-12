import sys; input = sys.stdin.readline

def main():
    tomatoes = get_inputs()
    print(solution(tomatoes))
    return

def get_inputs():
    m, n = map(int, input().split())
    tomatoes = [[-1 for _ in range(m+2)]]
    for _ in range(n):
        tomatoes.append([-1] + list(map(int, input().split())) + [-1])
    tomatoes.append([-1 for _ in range(m+2)])
    return tomatoes

def solution(tomatoes):
    answer = 0
    unriped = 0
    stack = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i, row in enumerate(tomatoes):
        for j, tomato in enumerate(row):
            if tomato == 0: unriped += 1
            if tomato == 1: stack.append((i, j))

    while stack:
        temp = []
        for tomato in stack:
            for i in range(len(dx)):
                nx = tomato[0] + dx[i]
                ny = tomato[1] + dy[i]
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1
                    temp.append((nx, ny))
                    unriped -= 1
        stack = temp
        answer += 1
    
    if unriped != 0: 
        return -1

    return answer-1

main()
