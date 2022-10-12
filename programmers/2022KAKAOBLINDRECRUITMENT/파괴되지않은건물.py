def solution(board, skill):
    n, m = len(board), len(board[0])
    cumu = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for s in skill:
        sign = 1 if s[0] == 2 else -1
        start_x, start_y = s[1], s[2]
        end_x, end_y = s[3], s[4]
        power = s[5]
        
        cumu[start_x][start_y] += sign * power
        cumu[start_x][end_y+1] -= sign * power
        cumu[end_x+1][start_y] -= sign * power
        cumu[end_x+1][end_y+1] += sign * power
        
    for i in range(n):
        for j in range(m):
            cumu[i][j+1] += cumu[i][j]
            
    for j in range(m):
        for i in range(n):
            cumu[i+1][j] += cumu[i][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + cumu[i][j] > 0: answer += 1
    
    return answer

"""
- 누적합
- 아래와 같은 2차원 배열은
    n n n 0
    n n n 0
    n n n 0
    0 0 0 0
  아래와 같은 2차원 배열의 누적합으로 표현할 수 있다.
    n 0 0 -n
    0 0 0 0
    0 0 0 0
    -n 0 0 n
  위 행렬을 행방향, 열방향 각각 한번씩 누적합을 적용
- n^2개의 원소들을 매번 모두 접근할 필요 없이 4개의 꼭지점만 접근해주면 됨
  더해줘야할 행렬이 많아지면 효과적이다.
"""
