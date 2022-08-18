import sys
input = sys.stdin.readline

def main():
    n = int(input())
    bricks = [(0, 0, 0, 0)]
    for i in range(1, n+1):
        s, h, w = map(int, input().split())
        bricks.append((i, s, h, w))
    bricks.sort(key=lambda x: x[1])

    memo = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i):
            if bricks[j][3] < bricks[i][3]:
                memo[i] = max(memo[i], memo[j] + bricks[i][2])

    max_h = max(memo)
    i = n
    ans = []
    while max_h != 0:
        if max_h == memo[i]:
            ans.append(bricks[i][0])
            max_h -= bricks[i][2]
        i -= 1

    print(len(ans))
    for e in reversed(ans):
        print(e)

main()

"""
- 벽돌들을 순서 인덱스를 포함하여 저장한다. 이후 편의를 위해 넓이, 무게, 높이가 0인
  0번 벽돌을 맨앞에 추가해준다.
- 벽돌들을 면적 또는 무게를 기준으로 오름차순 정렬한다 (위 코드의 경우 면적 기준)
- memo[i]는 bricks[i] 벽돌이 제일 밑에 깔렸을 때 얻을 수 있는 최대 높이다.
- memo[i] 계산 과정: 
    - bricks[i]를 맨 밑에 깔고 싶다.
    - i보다 작은 j에 대해 memo[j]를 쭉 본다. 
    - bricks[i]와 bricks[j]를 비교하여 bricks[i]가 bricks[j]보다 넓이는 크고 무게는
      작다면(이미 bricks가 넓이 기준으로 정렬되어 있기 때문에 무게만 비교하면 된다),
      bricks[i]를 맨 밑에 깔고 그 위에 memo[j] 덩어리를 올려서 높이를 memo[i]에
      넣는다.
    - 모든 memo[j]를 봐서 제일 높이가 커질 수 있는 값에 대해 memo[i]를 넣는다.
- memo 중 가장 큰 값을 이루는 벽돌들을 찾아가는 과정
    - 최대 max_h인 memo[i]를 찾는다.
    - 제일 밑에 깔려있는 bricks[i]를 꺼내고 memo[i] - bricks[i]의 높이를 다음 
      max_h로 지정한다.
    - max_h가 0이 될 때까지 반복하여 밑에있는 벽돌들을 계속 꺼낸다.
- 꺼낸 벽돌들을 역순으로 출력한다.
"""
