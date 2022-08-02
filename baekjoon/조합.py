import sys; input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    answer = 1
    for i in range(n, n-m, -1):
        answer *= i
    for i in range(m, 0, -1):
        answer //= i  # /를 하면 오차가 발생할 수 있기 때문에 int 나눗셈인 // 사용
    print(answer)

main()
