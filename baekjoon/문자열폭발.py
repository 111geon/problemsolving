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

"""
- 스택
- 문자열을 보는 족족 스택에 삽입, 삽입을 할 때 마다 스택을 상태를 보면서 폭탄의 존재 여부를 확인
    - 있다면 폭탄만큼 스택 뒤쪽을 delete
- 폭탄의 존재 여부는 스택을 peek하였을 때 문자가 폭탄의 가장 뒤 문자와 동일하다면, 폭탄의 글자수
  만큼 스택 뒤쪽을 들여다보면서 폭탄인지 확인하는 방법이 있다. 이때 당연히 스택은 폭탄보다 클것.
"""
