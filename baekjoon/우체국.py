import sys; input = sys.stdin.readline

def main():
    N = int(input())
    X = []
    A = []

    for _ in range(N):
        x, a = map(int, input().split())
        X.append(x)
        A.append(a)

    answer = sys.maxsize
    pos = sys.maxsize
    for i in range(N):
        temp = 0
        for j in range(N):
            temp += abs(X[i]-X[j]) * A[j]

        if temp < answer:
            pos = X[i]
            answer = temp
        
        if temp == answer:
            pos = min(pos, X[i])

    print(pos)

main()
