import math

def solution(n, k):
    q = []
    while n > 0:
        q = [n % k] + q[:]
        n //= k
    m = "".join(map(str, q))
    nums = []
    for mm in m.split('0'):
        if not mm: continue
        nums.append(int(mm))
    
    answer = 0
    for num in nums:
        if is_prime(num): answer += 1
    
    return answer

def is_prime(num):
    if num == 1: return False
    if num == 2: return True
    limit = int(math.sqrt(num))
    for i in range(2, limit+1):
        if num % i == 0: return False
    return True
    

# def make_seive(max_num):
#     if max_num == 1: return set()
#     if max_num == 2: return set([2])
#     ls = [2, 3]
#     while ls[-1] < max_num:
#         ls.append(ls[-1] + 2)

#     diff = set()
#     limit = int(math.sqrt(max_num))
#     for num in ls:
#         if num > limit: break
#         if num in diff: continue
#         for d in range(num * num, max_num+1, num):
#             diff.add(d)
    
#     return set(ls).difference(diff)
