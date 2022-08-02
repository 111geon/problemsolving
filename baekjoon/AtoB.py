import sys; input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    ans = 0
    while True:
        if a == b: break
        if a > b:
            ans = -2
            break
        if b % 10 == 1:
            b //= 10
            ans += 1
        elif b % 2 == 0:
            b //= 2
            ans += 1
        else:
            if b > a:
                ans = -2
                break
    print(ans+1)

main()
