def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    dup = { i for i in lost if i in reserve }
    
    lost = lost - dup
    reserve = sorted(reserve - dup)
    
    for i in reserve:
        if i - 1 in lost: lost.remove(i-1)
        elif i + 1 in lost: lost.remove(i+1)
    
    return n - len(lost)
