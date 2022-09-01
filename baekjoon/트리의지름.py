import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]  
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        tree[a].append((b, c))

    two_top = [[0] for _ in range(n+1)]
    set_two_top(n, tree, two_top, 1)

    ans = 0
    for i in range(1, n+1):
        if not tree[i]: continue
        ans = max(ans, two_top[i][0] + two_top[i][1])
    print(ans)

def set_two_top(n, tree, two_top, curr):
    for child, length in tree[curr]:
        if len(two_top[child]) == 1: set_two_top(n, tree, two_top, child)
        two_top[curr].append(two_top[child][0] + length)
        two_top[curr].sort(reverse=True)
        two_top[curr] = two_top[curr][:2]

main()

"""
- dfs
- 각 노드는 가장 긴 다리 두개를 알아야 한다. (다리는 두개 이상일 수 있었다.)
- 각 노드는 자식 노드를 보며 자식 노드의 가장 긴 다리를 이용해 자신의 다리를 업데이트한다.
    - 항상 두개의 가장 긴 다리를 남기도록 하였다.
    - 리프 노드의 유일한 다리는 0이 되도록 하였다.
- 각 노드를 돌며 가장 긴 다리 두개의 합 중 가장 큰 값이 답이 된다.
"""
