def solution(triangle):
    answer = [triangle[0]]
    for i in range(1, len(triangle)):
        temp = [triangle[i][0] + answer[i-1][0]]
        for j in range(1, len(triangle[i])-1):
            temp.append(max(answer[i-1][j-1], answer[i-1][j]) + triangle[i][j])
        temp.append(triangle[i][-1] + answer[i-1][-1])
        answer.append(temp)
    return max(answer[-1])
