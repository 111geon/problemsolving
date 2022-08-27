import sys; input = sys.stdin.readline
import heapq

def main():
    n = int(input())
    classes = []
    for _ in range(n):
        classes.append(tuple(map(int, input().split())))  # (s, t)
    classes.sort()

    hq = [0]  # t 기준
    ans = 1
    for s, t in classes:
        if s >= hq[0]: heapq.heappop(hq)
        else: ans += 1
        heapq.heappush(hq, t)

    print(ans)

main()

"""
- 그리디, 힙
- 수업(시작시간, 끝시간)들을 시작시간을 기준으로 정렬한다.
- 힙에는 수업의 끝시간을 넣는다.
- 힙에서 pop한 시간은 현재 시점에서 가장 금방 끝날 수업의 끝시간을 의미한다. 
- 내가 현재 새로 힙에 넣으려는 수업의 시작시간이 이전 수업들 중 가장 금방 끝날 수업의 끝시간보다
  뒤에 있다면 그 끝날 수업이 사용하던 강의실을 사용하면 되기 때문에 새로 강의실을 추가할 필요가
  없다. 그리고 그 끝날 수업은 이제 끝났기 때문에 힙에서 pop한다.
- 새로 넣을 수업의 시작시간이 가장 빨리 끝날 수업의 끝시간보다 이르다면 강의실을 하나 추가해야한다.
"""
