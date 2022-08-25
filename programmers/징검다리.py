def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + sorted(rocks) + [distance]
    
    lower, upper = 0, distance
    min_gap = (lower + upper) // 2
    
    while lower != min_gap:
        crushed_rocks = 0
        idx_checkpoint = 0
        
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[idx_checkpoint] < min_gap:
                crushed_rocks += 1
            else:
                idx_checkpoint = i
        
        if crushed_rocks > n:
            upper = min_gap
        else:
            lower = min_gap
        min_gap = (upper + lower) // 2
    
    return min_gap

# Greedy한 방식으로는 불가능 (ex. solution(16 , [4, 8, 11], 2) == 8)
# min_gap을 먼저 설정하고 맨 앞 돌부터 부셔나가면서 완전 탐색을 해야하는데 이를 이분 탐색으로 수행

# 2 11 14 17 21 25
# candidate = 5 -> n = 3
# candidate = 6 -> n = 3
# candidate = 7 -> n = 4
# candidate = 9 -> n = 4
# candidate = 10 -> n = 4
# candidate = 11 -> n = 4

# 4 8 11 16
