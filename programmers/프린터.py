from collections import deque

def solution(priorities, location):
    answer = 1
    p = deque(zip(range(len(priorities)), priorities))
    while(p):
        j = p.popleft()
        for k in p:
            if k[1] > j[1]:
                p.append(j)
                j = None
                break
        if j :
            if j[0] == location:
                return answer
            else:
                answer += 1
