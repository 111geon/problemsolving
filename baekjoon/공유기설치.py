import sys
input = sys.stdin.readline

def main():
    n, c = map(int, input().split())
    homes = []
    for _ in range(n):
        homes.append(int(input()))
    homes.sort()

    left = 1
    right = (homes[-1] - homes[0]) // (c - 1)
    while left < right:
        mid = (left + right + 1) // 2
        if possible(homes, n, c, mid): left = mid
        else: right = mid - 1

    print(left)

def possible(homes, n, c, gap):
    temp = homes[0]
    c -= 1
    
    for i in range(1, n):
        if homes[i] - temp >= gap:
            temp = homes[i]
            c -= 1

    if c <= 0: return True
    return False

main()

"""
- 공유기 사이 거리의 하한을 gap이라고 하고 이 gap을 이분탐색을 통해 최대값을 찾아간다
- 이 gap의 최소값은 1, 최대값은 가장 멀리 떨어져있는 두 집 사이 거리를 공유기 수 - 1
  만큼 나눈 값이다.
- 이 최소값과 최대값을 left와 right로 두고 이분탐색을 수행한다.
- mid를 gap으로 했을 때 모든 공유기 설치가 가능하다면 gap을 더 늘려보기 위해 left를
  mid로 대체한다.
- mid gap에 대하여 공유기 설치가 불가능하다면 gap을 줄이기 위해 right를 mid - 1로
  대체한다.
- 이 이분탐색이 끝나면 left가 최적의 gap이다.
- right - left가 1일 때 mid 는 right가 되도록 mid = (left + right + 1) // 2로 
  설정하였다. 이때 mid가 가능하다면 left가 right로 이동할 것이며, mid가 불가능하다면
  right가 left로 이동할 것이다.
- 공유기 설치가 가능한지 판단하는 건 정렬된 homes를 순회하면서 공유기를 놓을 수 있을
  때 마다(공유기 간격이 gap보다 크거나 같으면) 공유기를 하나씩 놓고(c -= 1) 공유기를
  다 놓았을 때 c가 0보다 작거나 같다면 공유기 설치가 가능, c가 0보다 크다면 공유기를
  미처 다 놓지 못한 것이므로 불가능한 것으로 판단한다.
"""
