import sys; input = sys.stdin.readline

def main():
    answer = 0
    s = "+" + input() + "+"
    i, j = 0, 1
    flip = 1
    while (j < len(s)):
        while (s[j] not in ("+", "-")): 
            j += 1
        if s[i] == "+":
            answer += flip * int(s[i:j])
        else:
            flip = -1
            answer += int(s[i:j])
        i = j
        j += 1
    print(answer)

main()
