import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    truth_init = []
    for i in map(int, input().split()[1:]):
        truth_init.append(i)

    group = [i for i in range(n+1)]
    group_children = [set([i]) for i in range(n+1)]
    
    parties = []
    for _ in range(m):
        party = list(map(int, input().split()[1:]))
        parties.append(party)
        for i in range(1, len(party)):
            a, b = party[i-1], party[i]
            temp = group[b]
            group_children[group[a]].update(group_children[group[b]])
            for child in group_children[group[b]]:
                group[child] = group[a]
            if group[a] != temp: group_children[temp].clear()

    truth = set()
    for i in truth_init:
        truth.update(group_children[group[i]])

    ans = 0
    for party in parties:
        for person in party:
            if person in truth: break
        else: ans += 1

    print(ans)

main()

"""
- union-find
- 이야기의 진실을 이미 알고있는 truth_init을 생성
- 사람 i가 자신이 속한 그룹을 나타내는 group과 그룹 i가 포함하는 사람들 집합을 
  나타내는 group_children을 생성
- 파티에 속한 사람들을 bubble로 비교하면서 두 사람의 그룹을 통합
    - 우선 group_children을 한쪽으로 통합하고 그 이후 group을 업데이트
    - 빠져나간 group_children은 clear -> 안해도 되긴 함
- 초기 진실을 아는 사람이 속하는 그룹에 있는 모든 사람들을 truth에 추가
- 모든 파티를 순회하며 한명이라도 truth에 포함된다면 거짓말을 못함
"""

