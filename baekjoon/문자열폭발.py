import sys; input = sys.stdin.readline

def main():
    str = input().strip()
    exp = list(input().strip())
    nstr = []
    for i in range(len(str)):
        nstr.append(str[i])
        if has_bomb(nstr, exp): del nstr[-len(exp):]
    if nstr: print("".join(nstr))
    else: print("FRULA")

def has_bomb(nstr, exp):
    if len(nstr) >= len(exp) and nstr[-1] == exp[-1] and nstr[-len(exp):] == exp:
        return True
    return False

main()
