import sys
sys.setrecursionlimit(1000000)

sysinput = sys.stdin.readline

def solution():
    num_test_case = int(sysinput())

    for _ in range(num_test_case):
        farm = construct_farm()
        print(count_worms(farm))

def construct_farm():
    m, n, num_cabbages = map(int, sysinput().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(num_cabbages):
        x, y = map(int, sysinput().split())
        farm[y][x] = 1

    return farm

def count_worms(farm):
    answer = 0

    for y in range(len(farm)):
        for x in range(len(farm[0])):
            if farm[y][x]:
                answer += 1
                visit_neigbors(farm, x, y)

    return answer

def visit_cabbage(farm, x, y):
    farm[y][x] = 0
    return

def visit_neigbors(farm, x, y):
    farm[y][x] = 0
    m ,n = len(farm[0]), len(farm)
    if x-1 >= 0 and farm[y][x-1]:
        visit_neigbors(farm, x-1, y)
    if x+1 < m and farm[y][x+1]:
        visit_neigbors(farm, x+1, y)
    if y-1 >= 0 and farm[y-1][x]:
        visit_neigbors(farm, x, y-1)
    if y+1 < n and farm[y+1][x]:
        visit_neigbors(farm, x, y+1)

solution()
