def main():
    n = int(input())
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    print(ans)

main()
