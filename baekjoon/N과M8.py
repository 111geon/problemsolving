import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    perm = []
    solution(nums, n, m, perm, 0)

def solution(nums, n, m, perm, start):
    if len(perm) == m:
        print(*perm)
        return
    for i in range(start, n):
        perm.append(nums[i])
        solution(nums, n, m, perm, i)
        perm.pop()

main()
