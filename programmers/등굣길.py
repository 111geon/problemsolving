def solution(m, n, puddles):
    pathes = [[1 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        pathes[puddle[1]-1][puddle[0]-1] = 0
    
    i, j, s = 1, 1, 2
    while s <= m + n:
        s += 1
        i = min(i+1, m)
        j = s - i
        k = 0
        while i-k >= 1 and j+k <= n:
            if pathes[j+k-1][i-k-1] == 0:
                pass
            elif j+k == 1:
                pathes[0][i-1] = pathes[0][i-2]
            elif i-k == 1:
                pathes[j-1][0] = pathes[j-2][0]
            else:
                pathes[j+k-1][i-k-1] = pathes[j+k-2][i-k-1] + pathes[j+k-1][i-k-2]
            k += 1
                
    return pathes[-1][-1] % 1000000007

print(solution(4, 3, [[2, 2]]))
print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)
print(solution(2, 1, []), 690285631)
