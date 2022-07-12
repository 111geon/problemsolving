from collections import deque

def solution(begin, target, words):
    visited = set()
    queue = deque()
    visited.add(begin)
    queue.appendleft((begin, 0))
    
    while queue:
        temp = queue.pop()
        begin, depth = temp[0], temp[1]
        for _next in words:
            if can_transfer(begin, _next) and _next not in visited:
                if _next == target: return depth+1
                visited.add(_next)
                queue.appendleft((_next, depth+1))
    return 0

def can_transfer(_from, _to):
    same_char = 0
    for i in range(len(_from)):
        same_char += 1 if _from[i] == _to[i] else 0
    if same_char == len(_from)-1:
        return True
    return False
