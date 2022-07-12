from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    on_bridge = deque([truck_weights.pop()])
    curr_t = 1
    starting_times = deque([curr_t])
    
    while(truck_weights):
        if sum(on_bridge) + truck_weights[-1] <= weight:
            curr_t += 1
            on_bridge.appendleft(truck_weights.pop())
            starting_times.appendleft(curr_t)
        else:
            on_bridge.pop()
            curr_t = max(starting_times.pop() + bridge_length - 1, curr_t)
        
    return curr_t + bridge_length

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.28ms, 10.2MB)
# 테스트 5 〉	통과 (0.79ms, 10.1MB)
# 테스트 6 〉	통과 (0.66ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.49ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.06ms, 10.1MB)
# 테스트 14 〉	통과 (0.00ms, 10.4MB)
