def solution(routes):
    answer = 0
    routes.sort(reverse=True)
    while routes:
        temp = routes.pop()
        answer += 1
        while routes:
            if routes[-1][0] > temp[1]:
                break
            temp[1] = min(temp[1], routes.pop()[1])
    return answer
