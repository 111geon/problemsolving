import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    nums = [str(x) for x in nums]
    solution(nums, n, m, [], 0, set())

def solution(nums, n, m, perm, start, trace):
    if len(perm) == m:
        temp = " ".join(perm)
        if temp not in trace:
            trace.add(temp)
            print(temp)
        return
    for i in range(start, n):
        perm.append(nums[i])
        solution(nums, n, m, perm, i, trace)
        perm.pop()

main()
