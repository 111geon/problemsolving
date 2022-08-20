import sys

input = sys.stdin.readline

def main():
    n = int(input())
    col = [False for _ in range(n)]
    diag1 = [False for _ in range(2*n)]
    diag2 = [False for _ in range(2*n)]
    ans = [0]
    n_queen(n, col, diag1, diag2, 0, ans)
    print(ans[0])

def n_queen(n, col, diag1, diag2, x, ans):
    if x == n:
        ans[0] += 1
        return
    for y in range(n):
        c, d1, d2 = y, x+y, x-y
        if col[c] or diag1[d1] or diag2[d2]: continue
        col[c], diag1[d1], diag2[d2] = True, True, True
        n_queen(n, col, diag1, diag2, x+1, ans)
        col[c], diag1[d1], diag2[d2] = False, False, False

main()

"""
- 좀 더 빠른 backtracking
- 기존의 퀸들과 비교하며 가는 방식이 아니라 퀸을 새로 놓을 때마다 visited를 갱신해나가는 방식
    - col[y좌표] = True 라면 해당 y좌표를 차지하는 퀸이 존재한다.
    - diag1[x좌표 + y좌표] = True 라면 x + y 대각선에 퀸이 존재한다.
        - (0, n), (1, n-1), (2, n-2), ..., (n, 0)은 모두 한 대각선에 존재한다.
    - diag2[x좌표 - y좌표] = True 라면 x - y 대각선에 퀸이 존재한다.
        - (0, 0), (1, 1), (2, 2), ..., (n, n)은 모두 한 대각선에 존재한다.
    - diag visited는 크기가 2n이 필요하다.
"""

# -----------------------------------------------------------------------------

def main():
    n = int(input())
    print(n_queen(n, [0 for _ in range(n)], 0))

def n_queen(n, queens, x):
    ans = 0
    if x == n: return 1
    for i in range(n):
        queens[x] = i
        if queen_possible(queens, x):
            ans += n_queen(n, queens, x+1)
    return ans

def queen_possible(queens, x):
    for i in range(x):
        if queens[i] == queens[x] or abs(queens[i] - queens[x]) == x - i:
            return False
    return True

main()

"""
- 기본적인 backtracking
- queens 배열: queens[board의 x 위치에서] = 존재하는 queen의 y 위치
- 하나의 x(row)에 들어갈 수 있는 퀸은 하나이기 때문에 하나의 x에서 y를 looping하며 퀸이 들어갈
  수 있는 자리를 찾는다.
- 이 자리를 찾을 때는 새로운 자리에 퀸을 놓았을 때 기존에 존재하는 queens와 비교하여 해당 자리에
  놓을 수 있는지 확인한다. 놓을 수 없다면 가지치기를 해버리는 방식.
    - 이때 이미 x는 겹칠 수 없으므로 y와 두개의 대각선을 비교한다.
    - y는 queens[i] == queens[x] 로 판정되고
    - 대각선은 x의 차이 == y의 차이 로 판정된다. x는 항상 i보다 크므로 x - i는 abs가 불필요
"""
