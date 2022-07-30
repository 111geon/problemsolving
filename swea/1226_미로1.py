def main():
    for _ in range(10):
        t = input()
        mat = []
        for _ in range(16):
            mat.append(list(input()))
        print("#" + t, solution(mat))
    
def solution(mat):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = [(1, 1)]
    mat[1][1] = '1'
    while stack:
        x, y = stack[-1]
        count = 0
        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if mat[nx][ny] == '3': return '1'
            if mat[nx][ny] == '1': 
                count += 1
                continue
            mat[nx][ny] = '1'
            stack.append((nx, ny))
        if count == 4:
            stack.pop()

    return '0'

main()
