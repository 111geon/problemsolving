import sys; input = sys.stdin.readline
import collections

def main():
    n, k = map(int, input().split())
    nums = list(input().split())

    answer = 0
    counts = collections.defaultdict(int)
    start, end = 0, 0

    while end < n:
        counts[nums[end]] += 1
        if counts[nums[end]] > k:
            answer = max(answer, end - start)
            counts[nums[start]] -= 1
            counts[nums[end]] -= 1
            start += 1
        else:
            end += 1

    answer = max(answer, end - start)
    print(answer)

main()

