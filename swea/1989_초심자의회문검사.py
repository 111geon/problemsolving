def main():
    n = int(input())
    for t in range(1, n+1):
        word = input().strip()
        print("#" + str(t) + " " + solution(word))

def solution(word):
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return '0'
    return '1'

main()
