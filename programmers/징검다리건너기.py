def solution(stones, k):    
    sorted_stones = sorted(stones)
    left, right = 0, len(stones) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if possible(stones, k, sorted_stones[mid]): left = mid
        else: right = mid - 1
    return sorted_stones[left]

def possible(stones, k, num):
    jump = 1
    for stone in stones:
        if stone - num < 0:
            jump += 1
            if jump > k: return False
        else: jump = 1
    return True

"""
- 이분탐색
- stones를 sort한다.
- stones의 값은 해당 stone이 0이 될때까지 건널 수 있는 사람의 수이다.
- 이 사람의 수를 늘렸다 줄였다 하면서 징검다리를 건널 수 있는지 확인하는 것이다.
"""