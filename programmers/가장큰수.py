from functools import cmp_to_key

def solution(numbers):
    def compare(a, b):
        if a+b > b+a:
            return -1
        else:
            return 1
    
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    return str(int("".join(numbers)))
