import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    s = []
    solution(1, n, m, s)

def solution(start, n, m, s):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n+1):
        s.append(i)
        solution(i, n, m, s)
        s.pop()

main()
