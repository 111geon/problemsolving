def solution(number, k):
    answer = ''
    
    start = -1
    end = k
    for _ in range(len(number)-k):
        max_n = 0
        for j in range(start+1, end+1):
            if int(number[j]) > max_n:
                start = j
                max_n = int(number[j])
            elif number[j] == '9': break
        end += 1
        answer += str(max_n)
    
    return answer
