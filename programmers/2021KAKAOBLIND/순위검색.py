def solution(info, query):
    answer = []
    languages = ["cpp", "java", "python"]
    positions = ["backend", "frontend"]
    careers = ["junior", "senior"]
    soulfoods = ["chicken", "pizza"]
    
    tree = {}
    for language in languages:
        for position in positions:
            for career in careers:
                for soulfood in soulfoods:
                    if language not in tree: 
                        tree[language] = {}
                    if position not in tree[language]: 
                        tree[language][position] = {}
                    if career not in tree[language][position]:
                        tree[language][position][career] = {}
                    if soulfood not in tree[language][position][career]:
                        tree[language][position][career][soulfood] = []
    
    for i in info:
        language, position, career, soulfood, score = i.split()
        tree[language][position][career][soulfood].append(int(score))
    
    for position_tree in tree.values():
        for career_tree in position_tree.values():
            for soulfood_tree in career_tree.values():
                for scores in soulfood_tree.values():
                    scores.sort()

    for q in query:
        language, _, position, _, career, _, soulfood, score = q.split()
        
        temp = 0
        for lan in languages if language == '-' else [language]:
            for pos in positions if position == '-' else [position]:
                for car in careers if career == '-' else [career]:
                    for sou in soulfoods if soulfood == '-' else [soulfood]:
                        temp += bin_search(tree[lan][pos][car][sou], int(score))
        answer.append(temp)
    
    return answer

def bin_search(ls, score):
    start, end = 0, len(ls)-1
    while start <= end:
        mid = (start + end) // 2
        if ls[mid] >= score:
            end = mid - 1
        else:
            start = mid + 1
    return len(ls) - start

"""
- 이진 탐색
- 가능한 조합들을 트리로 만들어서 점수들을 집어넣고 정렬
- query에 “-”이 있는 경우 전체 그룹 모두 순회
- 각 조합들에서 이진 탐색으로 기준 점수를 찾아 목표 점수 이상의 점수들의 수를 계산한다.
"""
