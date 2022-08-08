import sys
import itertools

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    chicken = []
    houses = []

    for i in range(n):
        row = input().split()
        for j in range(len(row)):
            if row[j] == "0": continue
            if row[j] == "1": houses.append((i, j))
            else: chicken.append((i, j))
    
    scores = []
    for chick in chicken:
        temp = []
        for house in houses:
            temp.append(abs(house[0] - chick[0]) + abs(house[1] - chick[1]))
        scores.append(temp)
    
    ans = sys.maxsize
    for comb in itertools.combinations(range(len(chicken)), m):
        score = 0
        for min_dist in map(min, (zip(*[scores[i] for i in comb]))):
            score += min_dist
            if score > ans: break
        ans = min(ans, score)

    print(ans)

main()

"""
- 백트래킹
- 각 치킨집을 기준으로 집들 과의 거리를 구해놓는다. -> scores
- m에 따른 치킨집 조합이 선정되면 해당하는 치킨집들 기준으로 scores로 부터 row들을 가져온다.
- 이 row들이 함께있는 2차원 리스트를 column 기준으로 묶었을 때 요소들 중 최소값이 house가
  가장 가까운 치킨집과의 거리를 나타내고, 이를 다 더한 것이 치킨 점수이다.
- 이 치킨점수들을 모든 조합에서 구해나간다. score를 합해 나갈 때 이 합이 현재까지의 ans를 넘어
  버린다면 더이상 계산할 필요 없이 가지치기를 해버린다.
"""
