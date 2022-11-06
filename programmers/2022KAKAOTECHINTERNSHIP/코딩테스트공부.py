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
