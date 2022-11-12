def solution(alp, cop, problems):
    a, c = 0, 0
    for problem in problems:
        a, c = max(a, problem[0]), max(c, problem[1])
    alp, cop = min(alp, a), min(cop, c)
    
    MAX_VAL = (1 << 63) - 1
    dp = [[MAX_VAL for _ in range(c+1)] for _ in range(a+1)]
    dp[alp][cop] = 0
    
    for ia in range(alp, a+1):
        for ic in range(cop, c+1):
            if ia+1 <= a: dp[ia+1][ic] = min(dp[ia+1][ic], dp[ia][ic]+1)
            if ic+1 <= c: dp[ia][ic+1] = min(dp[ia][ic+1], dp[ia][ic]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if ia < alp_req or ic < cop_req: continue
                na, nc = min(ia+alp_rwd, a), min(ic+cop_rwd, c)
                dp[na][nc] = min(dp[na][nc], dp[ia][ic] + cost)
                
    return dp[a][c]

"""
- dynamic programming, backpack
- 하나의 상태가 기존의 다른 상태들의 점화식으로 표현되기 때문에 DP 문제이다.
- 상태가 두 개의 정수인 요소의 조합으로 표현될 수 있으므로 백팩 문제이다.
- 목표점수가 현재점수보다 낮은 경우를 고려하여 경계조건을 적절히 설정해야함.
"""
