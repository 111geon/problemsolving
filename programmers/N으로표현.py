def solution(N, number):
    numbers_list = []
    for n in range(1, 9):
        numbers = set()
        numbers.add((10**n-1)*N//9)
        
        for i in range(n//2):
            for j in numbers_list[i]:
                for k in numbers_list[-1-i]:
                    numbers.add(j+k)
                    numbers.add(j*k)
                    if j-k != 0: numbers.add(abs(j-k))
                    if j//k != 0: numbers.add(j//k)
                    else: numbers.add(k//j)
        
        if number in numbers:
            return n
        
        numbers_list.append(numbers)
    
    return -1

"""
[[5], [55, 10, 25, 1]]
N 5

n = 1:
5

n = 2:
55 5+5 5-5 5*5 5/5

n = 3:
555 
55+5 55-5 5-55 55*5 55/5 5/55
(5+5)+5 (5+5)-5 5-(5+5) (5+5)/5 5/(5+5) (5+5)*5
5+5*5 5-5*5 5*5-5 5*5*5 5/(5*5) (5*5)/5
5+5/5 5-5/5 5*5/5 5/(5/5)

n = 4:
5555
N(1)+N(3) abs(N(1)-N(3)) N(1)*N(3) (N(1)/N(3) or N(3)/N(1))(if not 0)
N(2)+N(2) ...



1 = 5/5
2 = (5+5)/5
3 = (5+5+5)/5
4 = 5-5/5
5 = 5
6 = 5 + 5/5
7 = 5 + (5+5)/5
8 = 5 + (5+5+5)/5
9 = 5 + 5 - 5/5
10 = 5 + 5
11 = 55/5
12 = (55+5)/5
13 = (55+5+5)/5
14 = 5 + 5 + 5 - 5/5
15 = 5 + 5 + 5
16 = 55/5 + 5



"""
