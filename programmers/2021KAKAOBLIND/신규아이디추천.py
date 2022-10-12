def solution(new_id):
    letter_set = set(list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"))
    number_set = set(list("0123456789"))
    punctuation_set = set(list("-_."))
    allowed_set = letter_set.union(number_set).union(punctuation_set)
    
    answer = ""
    for letter in new_id:
        if letter not in allowed_set: continue
        if letter == '.' and answer and answer[-1] == '.': continue
        answer += letter.lower()
        
    answer = answer.strip('.')
    
    if len(answer) == 0: answer = "a"
    answer = answer[:15]
    if answer[-1] == '.': answer = answer[:-1]
    
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer

"""
- 문자열 처리
- 허용 가능한 문자들을 미리 정해주었다.
"""
