import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = 0, 0
block = [[]]

def solve(currx, curry, opx, opy):
    global block
    if block[currx][curry] == 0: return  # 죽는 조건
    curr_move = 0  # 짝수로 끝난다면 현재 플레이어 패배, 홀수면 승리
    block[currx][curry] = 0  # 앞으로 어디로든 이동할텐데 그땐 기존 자리 발판이 사라짐
    for dir in range(4):
        nx = currx + dx[dir]
        ny = curry + dy[dir]

        # 갈 수 없는 곳들
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if block[nx][ny] == 0: continue
        
        # current player가 swap되고 move 수가 1 증가한다.
        next_move = solve(opx, opy, nx, ny)+1 
        
        # 현재는 패배이나 다음 경로는 승리인 경우 현재의 move 수를 승리하는 경우의 move 수로 바꾼다. -> 승리를 위해 최선을 다한다.
        if curr_move % 2 == 0 and next_move % 2 == 1: curr_move = next_move 
        # 현재도 패배이고 다음도 패배라면 최대한 move 수를 늘린다. -> 질 수 밖에 없는 경우 최대한 늦게 진다.
        elif curr_move % 2 == 0 and next_move % 2 == 0: curr_move = max(curr_move, next_move)
        # 현재도 승리이고 다음도 승리라면 최대한 move 수를 줄인다. -> 이길 수 밖에 없는 경우 최대한 빨리 이긴다.
        elif curr_move % 2 == 1 and next_move % 2 == 1: curr_move = min(curr_move, next_move)

    block[currx][curry] = 1  # 발판 복구 후 다른 쪽 DFS
    return curr_move

def solution(board, aloc, bloc):
    global n, m, block
    n = len(board)
    m = len(board[0])
    block = copy.deepcopy(board)
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])

"""
- minmax tree
- solve 함수에 들어가는 x, y위치를 바꿔주면서 player가 바뀌는 효과를 내준다.
- 주석 참고
"""
