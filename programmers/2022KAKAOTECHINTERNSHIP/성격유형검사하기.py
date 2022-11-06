def solution(survey, choices):
    scores = dict()
    for type in list("ANCFMJRT"):
        scores[type] = 0
    for i in range(len(choices)):
        score = choices[i] - 4
        if score > 0: scores[survey[i][1]] += score
        elif score < 0: scores[survey[i][0]] -= score
    
    answer = ""
    for t1, t2 in ("RT", "CF", "JM", "AN"):
        if scores[t1] >= scores[t2]: answer += t1
        else: answer += t2
        
    return answer

"""
- 문자열처리, hash table
- 특이사항 없음
"""
