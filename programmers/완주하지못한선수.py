def solution(participant, completion):
    d = {}
    
    for i in participant:
        if i not in d: d[i] = 1
        else: d[i] += 1
    
    for i in completion:
        if d[i] == 1: d.pop(i)
        else: d[i] -= 1
    
    return list(d.keys())[0]
