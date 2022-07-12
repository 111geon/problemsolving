import sys; input = sys.stdin.readline

def main():
    _, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    perm = []
    solution(nums, m, perm)

def solution(nums, m, perm):
    if len(perm) == m:
        print(*perm)
        return
    for num in nums:
        if num not in perm:
            perm.append(num)
            solution(nums, m, perm)
            perm.pop()

main()
