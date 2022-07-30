import sys; input = sys.stdin.readline
import collections

def main():
    n, _, k, c = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(int(input()))
    sushi.extend(sushi[:k-1])

    eaten = collections.defaultdict(int)
    eaten[c] += 1
    for i in range(k):
        eaten[sushi[i]] += 1
    
    answer = len(eaten)
    for i in range(n-1):
        eaten[sushi[i]] -= 1
        if eaten[sushi[i]] == 0: eaten.pop(sushi[i])
        eaten[sushi[i+k]] += 1
        answer = max(answer, len(eaten))
    
    print(answer)

main()
