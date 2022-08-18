import sys; input = sys.stdin.readline

# 향상된 DP 풀이
def main():
    n, k = map(int, input().split())
    k += 1
    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        temp = {}
        for v_bag, w_bag in bag.items():
            nw = w + w_bag
            nv = v + v_bag
            if bag.get(nv, k) > nw:
                temp[nv] = nw
        bag.update(temp)

    print(max(bag.keys()))

# DP 풀이
def main():
    n, k = map(int, input().split())
    bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for ni in range(1, n+1):
        w, v = map(int, input().split())
        for wi in range(1, k+1):
            if w > wi:
                bag[ni][wi] = bag[ni-1][wi]
            else:
                bag[ni][wi] = max(bag[ni-1][wi-w]+v, bag[ni-1][wi])

    print(bag[-1][-1])

main()

"""
- 2차원 DP: dp[n][w] -> n번째 물건까지 넣을 때 무게 w를 갖는 가방의 최대 가치
      1 2 3 4 5  6   7 (w)..
    1 0 0 0 0 0  13  13
    2 0 0 0 8 8  13  13
    3 0 0 6 8 8  13  14
    4 0 0 6 8 12 13  14
    (n)
- dp[n][w] 계산 방법: dp[n-1][w - n번째 물건의 무게]에 n번째 물건을 넣으면 무게가 딱 맞을
  것이다. 이렇게 n번째 물건을 추가했을 때의 가치와 그냥 n-1번째 물건들로 w 무게까지 채운 가방의
  가치를 비교하여 더 큰 값을 넣는다.
- w - n번째 물건의 무게가 음수여서 dp가 없다면 그냥 dp[n-1][w]을 가져오면 될 것이다.
"""
