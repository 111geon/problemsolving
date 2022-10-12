answer = [-1]
max_diff = 0
max_idx = 0

def solution(n, info):
    dfs(info, n, 0, 0, 0, [], 0)
    if max_diff == 0: return [-1]
    return answer

def dfs(info, n, idx, score_ryan, score_apeach, result, highest_idx):
    global max_diff, answer, max_idx
    if n == 0 and score_ryan - score_apeach < max_diff: return
    if idx == 10:
        if score_ryan - score_apeach >= max_diff:
            if score_ryan - score_apeach == max_diff and highest_idx < max_idx:
                return
            max_diff = score_ryan - score_apeach
            answer = result[:] + [n]
            max_idx = highest_idx
        return
    if n > info[idx]: 
        dfs(info, n - info[idx] - 1, idx + 1, score_ryan + 10 - idx, score_apeach, result + [info[idx]+1], idx)
    if info[idx] == 0:
        dfs(info, n, idx + 1, score_ryan, score_apeach, result + [0], highest_idx)
    else:
        dfs(info, n, idx + 1, score_ryan, score_apeach + 10 - idx, result + [0], highest_idx)

"""
- dfs
- 가장 높은 점수부터 화살 한개를 더 넣어서 점수를 얻거나 아예 포기하거나를 선택
    - 화살 한개를 더 넣을 수 있을 때만 넣도록 조건을 써야할 것
    - 점수를 포기하는 경우 둘다 점수를 얻지 못하는 상황을 고려해야할 것.
- 점수 차이가 가장 클 때 가장 작은 점수를 얻은 경우를 정답에 넣어야함을 고려
"""
