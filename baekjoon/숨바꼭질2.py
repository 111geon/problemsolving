import sys; input = sys.stdin.readline
import collections

def main():
    n, k = map(int, input().split())
    if n > k:
        print(n-k)
        print(1)
        return

    q = collections.deque()
    q.appendleft((n, 0))
    ans = 0
    max_move = (1 << 63) - 1
    v = set()

    while q:
        pos, move = q.pop()
        if move > max_move: continue
        if pos > 2 * k or pos < 0: continue
        if pos == k:
            max_move = move
            ans += 1
        v.add(pos)
        for npos in (pos+1, pos-1, 2*pos):
            if npos in v: continue
            q.appendleft((npos, move+1))

    print(max_move)
    print(ans)

main()

"""
- bfs
- n이 k 보다 크면 걸어서 뒤로 가야한다.
- 이미 방문한 자리를 가게되면 무조건 move가 많아지기 때문에 넘겨버린다.
- 방문위치가 k의 2배를 넘게되면 무조건 move가 많아진다.
"""
