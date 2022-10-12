def solution(play_time, adv_time, logs):
    play_time = convert_seconds(play_time)
    adv_time = convert_seconds(adv_time)
    
    timeline = [0 for _ in range(play_time+1)]
    for log in logs:
        log = log.split('-')
        timeline[convert_seconds(log[0])] += 1
        timeline[convert_seconds(log[1])] -= 1
    
    for i in range(len(timeline)-1):
        timeline[i+1] += timeline[i]
    
    _sum = 0
    for i in range(adv_time):
        _sum += timeline[i]
        
    max_sum = _sum
    answer = 0
    for i in range(play_time - adv_time):
        _sum -= timeline[i]
        _sum += timeline[i+adv_time]
        if _sum > max_sum:
            max_sum = _sum
            answer = i + 1
    
    h = f'{answer // 3600:0>2d}'
    answer %= 3600
    m = f'{answer // 60:0>2d}'
    s = f'{answer % 60:0>2d}'
    
    return h + ":" + m + ":" + s

def convert_seconds(time):
    hour, minute, second = map(int, time.split(':'))
    return 3600 * hour + 60 * minute + second

"""
- 누적합, 슬라이딩 윈도우
- 모든 시간들을 초로 변환하여 계산 후 최종 결과를 다시 시간으로 변환하여 반환
- 처음엔 logs를 시작 시간순으로 정렬하여 log들의 시작시간와 끝시간을 기준으로 나뉘는 구간들 별로 광고를 보는 사람의 수를 계산하고 이를 문제 계산에 활용하려고 했다.
    - 구현이 더 까다로울 뿐더라 logs의 수가 많은 것에 비해 전체 동영상의 재생 시간이 그렇게 길지 않아서 비효율적인 접근 방식이었다.
    - 전체 동영상을 1초 단위로 구간들을 나누고 각 구간들 별로 광고를 보는 사람의 수를 계산하여 문제 풀이에 활용하는 방식이 훨씬 깔끔하다.
- 누적합을 이용하여 각 log별로 시작 지점과 끝 지점에 +1, -1 표시를 해둔다.
- 모든 logs에 대하여 표시를 하고 누적합을 계산한다.
- 전체 동영상에 광고 동영상의 길이 만큼의 슬라이딩 윈도우를 만들고 1초씩 진행시켜 최대 광고 시청 시간을 구한다.
"""
