import sys; input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for num in a:
        for i in range(len(b)):
            if num >= b[i]: 
                b[i] = num
                break
        else:
            b.append(num)
    
    print(len(b))

main()
