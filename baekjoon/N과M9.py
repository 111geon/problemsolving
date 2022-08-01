import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    idxs = []
    trace = set()
    solution(nums, m, idxs, trace)

def solution(nums, m, idxs, trace):
    if len(idxs) == m:
        temp = " ".join([str(nums[i]) for i in idxs])
        if temp not in trace:
            print(temp)
            trace.add(temp)
        return
    for i in range(len(nums)):
        if i not in idxs:
            idxs.append(i)
            solution(nums, m, idxs, trace)
            idxs.pop()

main()
