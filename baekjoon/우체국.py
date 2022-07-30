import sys; input = sys.stdin.readline

def main():
    N = int(input())
    towns = []
    people = 0

    for _ in range(N):
        x, a = map(int, input().split())
        towns.append((x, a))
        people += a

    towns.sort(key=lambda x: x[0])
    mid = people / 2

    temp = 0
    for i in range(N):
        temp += towns[i][1]
        if temp >= mid:
            print(towns[i][0])
            break

main()
