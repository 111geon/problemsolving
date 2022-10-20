import sys
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
_board = [[]]
n, m = 4, 0
answer = sys.maxsize
cards = []
targets = {}  # {card: []}

def solution(board, r, c):
    global _board, n, m, cards, targets
    _board = board
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            card = board[i][j]
            if card == 0: continue
            if card not in cards: cards.append(card)
            if card not in targets: targets[card] = []
            targets[card].append((i, j))
    
    dfs(0, r, c, [False for _ in range(len(cards))], 0)
    return answer

def dfs(depth, x, y, visited, result):
    global answer, _board
    if result >= answer: return
    if depth == len(cards): answer = result
    for i in range(len(cards)):
        if visited[i]: continue
        card = cards[i]
        
        ax, ay = targets[card][0]
        bx, by = targets[card][1]
        toa, tob = min_move(x, y, ax, ay), min_move(x, y, bx, by)
        atob, btoa = min_move(ax, ay, bx, by), min_move(bx, by, ax, ay)
        
        visited[i] = True
        _board[ax][ay], _board[bx][by] = 0, 0
        dfs(depth+1, bx, by, visited, result + toa + atob + 2)
        dfs(depth+1, ax, ay, visited, result + tob + btoa + 2)
        _board[ax][ay], _board[bx][by] = card, card
        visited[i] = False

def min_move(x, y, dest_x, dest_y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.appendleft((x, y, 0))
    while True:
        x, y, move = q.pop()
        if x == dest_x and y == dest_y:
            return move
        
        for d in range(len(dx)):
            nx, ny = x + dx[d], y + dy[d]
            if OOB(nx, ny) or visited[nx][ny]: continue
            q.appendleft((nx, ny, move+1))
            visited[nx][ny] = True
        for nx, ny in ctrl_move(x, y):
            if visited[nx][ny]: continue
            q.appendleft((nx, ny, move+1))
            visited[nx][ny] = True
          
def ctrl_move(x, y):
    ans = []
    for d in range(len(dx)):
        nx, ny = x + dx[d], y + dy[d]
        if OOB(nx, ny): continue
        
        while not OOB(nx, ny) and _board[nx][ny] == 0:
            nx, ny = nx + dx[d], ny + dy[d]
        if OOB(nx, ny):
            nx, ny = nx - dx[d], ny - dy[d]
        ans.append((nx, ny))
    return ans

def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n 

"""
- dfs + bfs
- cards에는 짝지을 카드의 종류가 중복없이 들어가 있으며, targets에는 카드 종류: (x, y)가 있다.
- dfs 로직
    - 목표로 갈 카드의 종류를 골랐을 때 카드가 위치하는 두 곳을 A, B라 한다.
    - 현재 위치에서 A, B로 가는 최소 비용, A에서 B, B에서 A로 가는 비용을 구한다.
    - 우선 A를 갔다가 B로 가는 경우와 B로 갔다가 A로 가는 경우를 각각 dfs
- 최소 비용 계산 로직 (bfs)
    - 현재 위치에서 4방향으로 이동함. OOB면 넘기기. 이동한 위치들 큐에 삽입
    - 컨트롤 이동한 위치들 큐에 삽입
        - 이동 방향으로 OOB나 0이 나올 때까지 계속 이동.
        - OOB면 한칸 되돌아옴, 아니면 그자리가 새로운 자리
    - visited를 처리해줘야 불필요한 경로를 가지 않는다.
"""
