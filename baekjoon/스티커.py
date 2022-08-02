import sys; input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n = int(input())
        nums = []
        nums.append(list(map(int, input().split())))
        nums.append(list(map(int, input().split())))

        dp_up = nums[0][0]
        dp_down = nums[1][0]
        dp_none = 0

        for i in range(1, n):
            dp_up_next = max(dp_down, dp_none) + nums[0][i]
            dp_down_next = max(dp_up, dp_none) + nums[1][i]
            dp_none_next = max(dp_up, dp_down)
            dp_up, dp_down, dp_none = dp_up_next, dp_down_next, dp_none_next

        print(max(dp_up, dp_down, dp_none))

main()
