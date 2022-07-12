import math

def solution(n, times):
    t_start = min(times)
    t_end = t_start * n
    
    for _ in range(-int(-math.log2(t_end - t_start + 1)) + 1):
        t = (t_start + t_end) // 2
        div = 0
        
        for time in times:
            div += t // time
            
        if div >= n:
            t_end = t
            
        else:
            t_start = t

    if div < n:
        return t+1
    else:
        return t
