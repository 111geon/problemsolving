import sys; sysinput = sys.stdin.readline

def find_bags(N):
    five = N // 5
    while five >= 0:
        three = N - 5 * five
        if three % 3 == 0:
            three //= 3
            return three + five
        five -= 1
    return -1

N = int(sysinput())
print(find_bags(N))