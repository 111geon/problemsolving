from collections import deque

def solution(people, limit):
    answer = 0
    
    if len(people) == 1:
        return 1
    
    people = deque(sorted(people))
    heavyone = people.pop()
    lightone = people.popleft()
    
    while(people):
        answer += 1
        if heavyone + lightone <= limit:
            lightone = people.popleft()
        if people: heavyone = people.pop()
    
    if heavyone + lightone > limit: answer += 1

    return answer + 1
