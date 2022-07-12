def solution(progresses, speeds):
    answer = []
    
    days = [ -(-(100-progresses[i])//speeds[i]) for i in range(len(progresses)) ]
    
    bar = 0
    for day in days:
        if day > bar:
            bar = day
            answer.append(1)
        else:
            answer[-1] += 1
    
    return answer
