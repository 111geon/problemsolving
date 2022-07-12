from math import sqrt

def solution(brown, yellow):
    a = 1
    while a <= sqrt(yellow):
        if yellow % a != 0:
            a += 1
            continue
        
        b = yellow / a
        if brown == (a + b + 2) * 2:
            return [b+2, a+2]
        a += 1
    return 1


# def solution(brown, yellow):
#     i = ((brown/2-2)+sqrt((brown/2-2)**2-4*yellow))/2
#     return [i+2, yellow/i+2]
