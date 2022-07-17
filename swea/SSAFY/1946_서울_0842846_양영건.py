def main():
    n = int(input())
    for t in range(1, n+1):
        print("#" + str(t))
        solution()

def solution():
    n = int(input())
    line = ""
    for _ in range(n):
        letter, num = input().split()
        line += letter * int(num)
        while len(line) > 10:
            print(line[:10])
            line = line[10:]
    print(line)

main()
