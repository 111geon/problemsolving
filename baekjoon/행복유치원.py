import sys; input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))

    diffs = []
    for i in range(1, n): diffs.append(heights[i] - heights[i-1])
    diffs.sort()
    print(sum(diffs[:n-k]))

main()

"""
- 그리디 알고리즘
- 정렬된 학생들의 앞뒤 키 차이들 중 가장 큰 값을 찾는다.
    - 해당 부분이 끊어지면서 두 그룹으로 나뉘면 가장 큰 비용 절감 효과를 얻는다.
- k-1 번의 끊는 행위를 수행하면 k개의 그룹이 생성된다.
    - 총 비용 = 키 차이 값들의 전체 합 - 끊어서 제외시켜 버린 키 차이 값들의 합
- 결국 diffs를 정렬해서 k개의 가장 큰 뒤부분을 잘라낸 배열의 합을 구하는 것과 같다.
"""
