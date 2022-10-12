import collections
import math

def solution(fees, records):
    cumul_times = collections.defaultdict(int)
    times = dict()
    for record in records:
        time, num, inout = record.split()
        hour, minute = map(int, time.split(":"))
        minutes = 60 * hour + minute
        if inout == "IN": 
            times[num] = minutes
        else:
            cumul_times[num] += minutes - times[num]
            times[num] = -1
    
    for num, time in times.items():
        if time == -1: continue
        cumul_times[num] += 23 * 60 + 59 - time
    
    answer = []
    for num in sorted(cumul_times):
        money = fees[1]
        time = cumul_times[num]
        if time <= fees[0]: 
            answer.append(money)
            continue
        time -= fees[0]
        time /= fees[2]
        time = math.ceil(time)
        money += time * fees[3]
        answer.append(money)
    
    return answer

"""
- 문자열 처리 + 해시
- 딕셔너리에 총 주차한 분을 저장하고 규칙대로 요금을 계산한다.
"""
