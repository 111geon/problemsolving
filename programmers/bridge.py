from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = list(reversed(truck_weights))
    on_bridge = deque([truck_weights.pop()])
    curr_t = 1
    starting_times = deque([curr_t])
    
    while(on_bridge and truck_weights):
        if len(on_bridge) < bridge_length and sum(on_bridge) + truck_weights[-1] <= weight:
            curr_t += 1
            on_bridge.appendleft(truck_weights.pop())
            starting_times.appendleft(curr_t)
        else:
            on_bridge.pop()
            curr_t = starting_times.pop() + bridge_length - 1

    return curr_t

print(solution(2, 10, [7,4,5,6]))
