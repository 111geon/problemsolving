MAX = (1 << 31) - 1
tree =  [[]]
dp = [[]]
sales = []

def solution(_sales, links):
    global tree, dp, sales
    sales = _sales
    
    tree = [[] for _ in range(len(sales))]
    for boss, sub in links:
        tree[boss-1].append(sub-1)
        
    dp = [[MAX, MAX] for _ in range(len(sales))]
    dfs(0)
    return min(dp[0][0], dp[0][1])

def dfs(boss):
    global dp
    if not tree[boss]: 
        dp[boss] = [sales[boss], 0]
        return
    for sub in tree[boss]: 
        dfs(sub)
        
    dp[boss][0] = sales[boss] + sum([min(dp[sub][0], dp[sub][1]) for sub in tree[boss]])
    
    temp = MAX
    for sub_first in tree[boss]:
        temtemp = dp[sub_first][0]
        for sub_second in tree[boss]:
            if sub_second == sub_first: continue
            temtemp += min(dp[sub_second][0], dp[sub_second][1])
        temp = min(temp, temtemp)
    dp[boss][1] = temp

"""
- 트리 dfs + dp
- 제일 보스부터 dfs를 시작한다. dfs는 dp를 업데이트하는 일을 한다.
- dp[n]의 0번째 원소는 n이 회의에 참석했을 때의 최소값이다. (부하들은 회의에 참여하던말던 상관없음 작은걸 가져옴)
- 1번째 원소는 n이 회의에 참석하지 않았을 때의 최소값이다.
    - 최소 한명의 부하는 참석을 해야하는 상황이다.
    - sub_first는 무조건 참석을 하는 부하를 의미하며
    - 이를 제외한 부하들은 참석하던 말던 상관없으니 최소값을 가져와서 더해준다.
- 부하가 없는 말단 부하의 경우 참석하는 경우 자신의 비용이, 아닌 경우 비용은 0이다.
- 보스의 dp를 알기위해선 부하들의 dp를 모두 알아야하기 때문에 우선 dfs를 최대한 깊이 들어간 후 올라오면서 dp를 업데이트한다.
"""
