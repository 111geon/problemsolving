import sys; input = sys.stdin.readline

# 향상된 DP 풀이
def main():
    n, k = map(int, input().split())
    k += 1
    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        temp = {}
        for v_bag, w_bag in bag.items():
            nw = w + w_bag
            nv = v + v_bag
            if bag.get(nv, k) > nw:
                temp[nv] = nw
        bag.update(temp)

    print(max(bag.keys()))

# DP 풀이
def main():
    n, k = map(int, input().split())
    bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for ni in range(1, n+1):
        w, v = map(int, input().split())
        for wi in range(1, k+1):
            if w > wi:
                bag[ni][wi] = bag[ni-1][wi]
            else:
                bag[ni][wi] = max(bag[ni-1][wi-w]+v, bag[ni-1][wi])

    print(bag[-1][-1])

main()
