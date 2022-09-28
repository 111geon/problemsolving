import sys; input = sys.stdin.readline

def main():
    n, h = map(int, input().split())
    down = []
    up = []
    for i in range(n):
        if i % 2 == 0: down.append(int(input()))
        else: up.append(int(input()))

    down.sort()
    up.sort()

    hits_of_level = []
    for i in range(1, h+1):
        hits = 0
        l, r = 0, n//2 - 1
        while l <= r:
            mid = (l + r) // 2
            if down[mid] < i:
                l = mid + 1
            else:
                r = mid - 1
        hits += n // 2 - l
        
        l, r = 0, n//2 - 1
        while l <= r:
            mid = (l + r) // 2
            if h - up[mid] >= i:
                l = mid + 1
            else:
                r = mid - 1
        hits += n // 2 - l
        hits_of_level.append(hits)

    # cumul_down = [0 for _ in range(h)]
    # cumul_up = [0 for _ in range(h)]

    # for i in range(n//2):
    #     cumul_down[down[i]-1] += 1
    #     cumul_up[h-up[i]] += 1
    
    # for i in range(h-1, 0, -1):
    #     cumul_down[i-1] += cumul_down[i]
    
    # for i in range(0, h-1):
    #     cumul_up[i+1] += cumul_up[i]

    # hits_of_level = list(map(sum, zip(cumul_down, cumul_up)))

    min_hits = min(hits_of_level)
    min_num = 0
    for hits in hits_of_level:
        if min_hits == hits:
            min_num += 1

    print(min_hits, min_num)

main()

"""
- 누적합
- up과 down은 장애물의 길이를 뜻한다.
- cumul_down과 cumul_up은 i 높이에서 부딪치게 되는 down과 up의 수이다.
    - 우선 up과 down으로부터 최고 높이 지점에서의 부딪치게되는 수에 +1을 해준다.
    - 모든 up과 down을 처리해주었다면 최고 높이부터 아래로 내려오며 부딪치게되는 수를 누적합으로 더해준다.
- cumul_down과 cumul_up을 합쳐주어 i 높이에서 부딪치게 되는 총 장애물 수를 구해준다.
- 최대값을 찾고 그 최대값에 해당하는 높이의 개수를 구해준다.

- 이진탐색
- 1 2 3 3 3 3 4 에서 제일 왼쪽 3 또는 제일 오른쪽 3을 선택하는 방법
    - value == key 일때 왼쪽오른쪽 어디로 갈지 결정
    - mid를 (left + right) // 2 로 할지 (left + right + 1) // 2로 할지 결정
    - while l <= r 은 고정..
"""
