def main():
    t = int(input())
    for tt in range(1, t+1):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(input().split())
        print('#' + str(tt))
        solution(n, matrix)

def solution(n, matrix):
    for i in range(n):
        print(degree90(n, matrix, i), degree180(n, matrix, i), degree270(n, matrix, i))

def degree90(n, matrix, start):
    result = ""
    for i in reversed(range(n)):
        result += matrix[i][start]
    return result

def degree180(n, matrix, start):
    result = ""
    for i in reversed(range(n)):
        result += matrix[-start-1][i]
    return result

def degree270(n, matrix, start):
    result = ""
    for i in range(n):
        result += matrix[i][-start-1]
    return result

main()
