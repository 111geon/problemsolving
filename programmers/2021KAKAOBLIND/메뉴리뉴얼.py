from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    comb_dict = {}  # {comb길이: {comb: comb개수}}
    for num in course:
        comb_dict[num] = defaultdict(int)
        
    for order in orders:
        for num in course:
            for comb in map("".join, combinations(sorted(order), num)):
                comb_dict[num][comb] += 1
                    
    for num_dict in comb_dict.values():
        if not num_dict: continue
        max_num = max(num_dict.values())
        if max_num < 2: continue
        for comb, num in num_dict.items():
            if num == max_num: answer.append(comb)
    
    return sorted(answer)

"""
- 조합
- 조합의 길이 별로 가장 많이 등장한 조합을 알아야하기 때문에 comb_dict의 키는 comb 길이가 되어야 한다. (문제 지문이 난해함)
    - 해당 키의 값들은 조합과 해당 조합이 등장한 수이다.
- 문제 조건에 맞게 처리해주고 answer에 조합을 추가
"""
