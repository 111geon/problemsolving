import sys; input = sys.stdin.readline

def main():
    n = int(input())
    ans = []
    dfs(10, [], ans)
    
    if n > len(ans):
        print(-1)
        return
    ans.sort()
    print(ans[n-1])

def dfs(end, nums, ans):
    for i in range(0, end):
        nums.append(str(i))
        ans.append(int("".join(nums)))
        dfs(i, nums, ans)
        nums.pop()

main()
