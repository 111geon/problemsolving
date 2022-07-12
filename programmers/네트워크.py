def solution(n, computers):
    answer = 0
    visited = set()
    stack = []
    for i in range(n):
        if i in visited: continue
        answer += 1
        visited.add(i)
        stack.append(i)
        while stack:
            j = stack.pop()
            for k in range(n):
                if computers[j][k] == 1 and k not in visited:
                    visited.add(k)
                    stack.append(k)
    return answer
