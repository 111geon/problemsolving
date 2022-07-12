import itertools
# print(list(itertools.permutations("1234", 3)))

def combinations(iterable, r):
    pool = tuple(iterable) # pool: "ABCDE"
    n = len(pool) # n: 5
    if r > n: # r: 3
        return
    indices = list(range(r)) # indices: [0, 1, 2]
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)): # i: [2, 1, 0]
            if indices[i] != i + n - r: # i + n - r: [4, 3, 2]
                break
        else:
            return

        # break된 i에서 index 1 증가
        indices[i] += 1

        # indices: [0, 3, 4]에서 i가 0일때 break 되서 indices[0]이 0 -> 1이 되면 indices를 [1, 2, 3]으로 만들어줌
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        yield tuple(pool[i] for i in indices)

# print(list(combinations("12345", 3)))

def permutations(iterable, r=None):
    pool = tuple(iterable) # pool: "ABCDE"
    n = len(pool) # n: 5
    r = n if r is None else r # r: 3
    if r > n:
        return
    indices = list(range(n)) # indices: [0, 1, 2, 3, 4]
    cycles = list(range(n, n-r, -1)) # cycles: [5, 4, 3]
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)): # i: [2, 1, 0]
            cycles[i] -= 1
            # [5, 4, 3] -> [5, 4, 2] -> [5, 4, 1] -> [5, 4, 0]
            # [5, 4, 3] -> [5, 3, 3] 
            # [5, 3, 3] -> [5, 3, 2] -> [5, 3, 1] -> [5, 3, 0]
            # [5, 3, 3] -> [5, 2, 3]
            # [5, 2, 3] -> [5, 2, 2] -> [5, 2, 1] -> [5, 2, 0]
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1] 
                # [0, 1, 4, 2, 3] -> [0, 1, 2, 3, 4]
                # [0, 2, 4, 1, 3] -> [0, 2, 1, 3, 4]
                # [0, 3, 4, 1, 2] -> [0, 3, 1, 2, 4]
                cycles[i] = n - i 
                # [5, 4, 0] -> [5, 4, 3]
                # [5, 3, 0] -> [5, 3, 3]
                # [5, 2, 0] -> [5, 2, 3]
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i] 
                # [0, 1, 2, 3, 4] -> [0, 1, 3, 2, 4] -> [0, 1, 4, 2, 3]
                # [0, 1, 2, 3, 4] -> [0, 2, 1, 3, 4] 
                # [0, 2, 1, 3, 4] -> [0, 2, 3, 1, 4] -> [0, 2, 4, 1, 3]
                # [0, 2, 1, 3, 4] -> [0, 3, 1, 2, 4]
                # [0, 3, 1, 2, 4] -> [0, 3, 2, 1, 4] -> [0, 3, 4, 1, 2]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

print(list(permutations("12345", 3)))

# ---

def combinations(arr,r):
    for i in range(len(arr)-r+1):
        if r == 1:
            yield arr[i:i+1]
        else:
            for comb in combinations(arr[i+1:], r-1):
                yield arr[i:i+1] + comb

print(list(combinations("1234", 3)))
# f(1234, 3): 1 + f(234, 2), 2 + f(34, 2)
# f(234, 2): 2 + f(34, 1), 3 + f(4, 1)
# f(34, 1): 3, 4

# ---

def permutation(ls, r):  
    for i in range(len(ls)):
        if r == 1:
            yield ls[i:i+1]
        else:
            for p in permutation(ls[:i] + ls[i+1:], r-1):
                yield ls[i:i+1] + p 

# print(list(permutation([1, 2, 3, 4], 3)))
# f([1, 2, 3, 4]): [1] + f([2, 3, 4]), [2] + f([1, 3, 4]), [3] + f([1, 2, 4]), [4] + f([1, 2, 3])
# f([2, 3, 4]): [2] + f([3, 4]), [3] + f([2, 4]), [4] + f([2, 3])
# f([3, 4]): [3] + f([4]), [4] + f([3])
# f([4]) = [[4]]
# f([3, 4]): [[3, 4], [4, 3]]
# f([2, 3, 4]): [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]
# f([1, 2, 3, 4]): [[1, 2, 3, 4], [1, 2, 4, 3], ...]

# ---

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

# print(list(all_perms("1234")))
# f(1234): 1을 떼서 f(234) 사이사이에 넣어줌
# f(234): 2를 떼서 f(34) 사이사이에 넣어줌
# f(34): 3을 떼서 f(4) 사이사이에 넣어줌
# f(4) = 4
# f(34): 34, 43
# f(234): 234, 324, 342, 243, 423, 432
# f(1234): 1234, 2134, 2314, 2341, 1324, ...

# 위 알고리즘은 r을 적용하지 못함.

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


