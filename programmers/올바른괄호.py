def solution(s):
    stack = []
    for ss in s:
        if not stack:
            stack.append(ss)
            continue
        if stack[-1] == "(" and ss == ")":
            stack.pop()
        else:
            stack.append(ss)
    if stack: return False
    return True
