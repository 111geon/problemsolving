import itertools
import math

def solution(numbers):
    answer = 0
    
    permutations = set()
    for i in range(len(numbers)):
        for p in itertools.permutations(numbers, i+1):
            number = int("".join(p))
            if number not in [0, 1] and number % 2 == 1 or number == 2:
                permutations.add(number)
    
    sieve = get_primes_under(math.ceil(math.sqrt(max(permutations))))
    
    for p in permutations:
        if p == 2:
            answer += 1
            continue
        for div in sieve:
            if p % div == 0:
                break
            elif div > math.sqrt(p):
                answer += 1
                break
        else:
            answer += 1
            
    return answer

def get_primes_under(number: int):
    if number < 2: 
        raise KeyError
    sieve = [2] + list(range(3, number+1, 2))
    high_bound = int(math.sqrt(number))

    for s in sieve[1:]:
        if s > high_bound:
            break
        else:
            sieved = s + s
            while(sieved<=number):
                if sieved in sieve: sieve.remove(sieved)
                sieved += s
                
    return sieve

# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (3.99ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (1.67ms, 10.5MB)
# 테스트 5 〉	통과 (17.57ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.07ms, 10.5MB)
# 테스트 8 〉	통과 (25.67ms, 10.4MB)
# 테스트 9 〉	통과 (0.04ms, 10.4MB)
# 테스트 10 〉	통과 (7.24ms, 10.5MB)
# 테스트 11 〉	통과 (0.95ms, 10.5MB)
# 테스트 12 〉	통과 (0.33ms, 10.4MB)

# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)

# 테스트 1 〉	통과 (0.51ms, 10.5MB)
# 테스트 2 〉	통과 (75.08ms, 44.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (51.13ms, 19.8MB)
# 테스트 5 〉	통과 (277.85ms, 145MB)
# 테스트 6 〉	통과 (0.04ms, 10.3MB)
# 테스트 7 〉	통과 (0.58ms, 10.3MB)
# 테스트 8 〉	통과 (740.85ms, 280MB)
# 테스트 9 〉	통과 (0.08ms, 10.4MB)
# 테스트 10 〉	통과 (409.46ms, 51.1MB)
# 테스트 11 〉	통과 (33.89ms, 13.5MB)
# 테스트 12 〉	통과 (5.71ms, 13.3MB)
