def solution(clothes):
    answer = 1

    dresses = dict()
    
    for c in clothes:
        if c[1] in dresses: dresses[c[1]] += 1
        else: dresses[c[1]] = 1
        
    for k, d in dresses.items():
        answer *= d + 1
    
    return answer - 1
