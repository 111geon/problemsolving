import sys; input = sys.stdin.readline

def main():
    string = input()
    temp = 0
    answer = 0
    for i in range(len(string)):
        if string[i] == '+':
            answer += int(string[temp:i])
        elif string[i] == '-':
            answer -= int(string[temp:i])
        temp = i
    print(answer)

main()

