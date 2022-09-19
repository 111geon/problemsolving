import sys; input = sys.stdin.readline

# 부분집합
# def main():
#     ls = ["계란", "참치", "김치", "단무지"]
#     powerset(ls, 0, [False for _ in range(4)])

# def powerset(ls, idx, s):
#     if idx == len(ls):
#         temp = []
#         for i in range(len(s)):
#             if s[i]: temp.append(ls[i])
#         print(*temp)
#         return
#     s[idx] = False
#     powerset(ls, idx+1, s)
#     s[idx] = True
#     powerset(ls, idx+1, s)
    
# main()

# 부분집합 비트마스킹

# def main():
#     n = 4
#     ls = ["계란", "참치", "김치", "단무지"]
#     for i in range(1 << n):
#         temp = []
#         for j in range(n):
#             if i & 1 << j > 0:
#                 temp.append(ls[j])
#         print(*temp)

# main()


# 중지 조건이 포함된 backtracking 재귀 (combinations)

# def getSequence(s, k, N, M, result):
#     if N - M + 1 < s - k: # N, M = 4, 3 에서 3으로 시작하는 배열은 아예 처음 시작부터 안하도록
#         return
#     if k == M:
#         print(*result)
#         return
#     for i in range(s, N + 1):
#         result.append(i)
#         getSequence(i + 1, k + 1, N, M, result)
#         result.pop()

# def main():
#     N, M = map(int, input().split())
#     result = []
#     getSequence(1, 0, N, M, result)

# main()

# ---

# backtracking 재귀 (combinations)

# def main():
#     n,m = list(map(int,input().split()))
#     s = []
#     dfs(1, n, m, s)

# def dfs(start, n, m, s):
#     if len(s) == m:
#         print(*s)
#         return
    
#     for i in range(start, n+1):
#         s.append(i)
#         dfs(i+1, n, m, s)
#         s.pop()

# static한 배열을 다루는 재귀 -> 하나의 추가적인 인덱스가 필요
def main():
    ls = ["a", "b", "c", "d"]
    n = 4
    m = 3
    combination(ls, n, m, ["", "", ""], 0, 0)

def combination(ls, n, m, s, idx, sidx):  # sidx는 s의 원소값을 업데이트하는 idx, idx는 ls에 해당하는 idx
    if sidx == m:
        print(*s)
        return
    for i in range(idx, n):
        s[sidx] = ls[i]
        combination(ls, n, m, s, i+1, sidx+1)

main()

# main()



# ---

# backtracking 재귀 (permutations)

# def main():
#     n,m = list(map(int,input().split()))
#     s = []
#     dfs(n, m, s)

# def dfs(n, m, s):
#     if len(s) == m:
#         print(*s)
#         return
    
#     for i in range(1, n+1):
#         if i not in s:
#             s.append(i)
#             dfs(n, m, s)
#             s.pop()

# main()

# ---

# 하향식 재귀

# def main():
#     n, m = map(int, input().split())
#     for comb in solution(1, n, m):
#         print(comb)


# def solution(start, end, r):
#     for i in range(start, end-r+2):
#         if r == 1:
#             yield str(i)
#         else:
#             for next in solution(i+1, end, r-1):
#                 yield str(i) + " " + next

# main()

# ---

# itertools library 이용

# import itertools

# n, m = map(int, input().split())

# for comb in itertools.combinations(range(1, n+1), m):
#     print(" ".join(map(str, comb)))
