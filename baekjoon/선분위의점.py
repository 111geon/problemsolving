import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    dots = [0] + sorted(list(map(int, input().split()))) + [sys.maxsize]
    for _ in range(m):
        start, end = map(int, input().split())
        print(bs_right(dots, end, 0, len(dots)-1) - bs_left(dots, start, 0, len(dots)-1) + 1)

def bs_right(dots, num, left, right):
    while True:
        mid = (right + left + 1) // 2
        if dots[mid] <= num:
            if dots[mid+1] > num: return mid
            left = mid + 1
        else:
            right = mid - 1

def bs_left(dots, num, left, right):
    while True:
        mid = (right + left + 1) // 2
        if dots[mid] >= num:
            if dots[mid-1] < num: return mid
            right = mid - 1
        else:
            left = mid + 1

main()

"""
- 이진 탐색으로 선분 안에 들어오는 가장 왼쪽 점과 가장 오른쪽 점의 인덱스를 찾는다.
- 이 두 인덱스의 차이 + 1이 선분안에 들어오는 점의 개수가 된다.
- 가장 오른쪽 점을 찾는 과정
    - 선분의 오른쪽 끝을 num이라고 할 때 선분안에 들어오는 가장 오른쪽 점은 num보다 작거나 같고
      그 점의 오른쪽에 있는 점은 num보다 크게 된다.
    - dots[mid]의 값이 num보다 크다면 right를 mid - 1로 바꾸어 dots[mid]를 줄여준다.
    - dots[mid]가 num보다 작다면 left를 mid + 1로 바꾸어 dots[mid]를 키워주어야 한다.
- num이 선분을 벗어나는 경우를 계산하기 위해 dots 앞뒤에 패딩을 붙여주어야 한다.
"""
