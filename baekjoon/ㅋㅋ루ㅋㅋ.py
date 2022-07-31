import sys; input = sys.stdin.readline

def main():
    krs = input().strip()
    n = len(krs)
    lk = []
    ks = 0
    for s in krs:
        lk.append(ks)
        if s == "K": ks += 1
    
    i, j = 0, n - 1
    ans = 0
    while i <= j:
        while krs[i] != "R" and i < n-1: i += 1
        while krs[j] != "R" and j > 0: j -= 1
        if i > j: break

        tmp = 2 * min(lk[i], ks - lk[j]) + (j - lk[j]) - (i - lk[i]) + 1
        ans = max(ans, tmp)

        if lk[i] > ks - lk[j]: j -= 1
        else: i += 1

    print(ans)

main()
