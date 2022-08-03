import sys; input = sys.stdin.readline

def main():
    n = int(input())
    maxa, maxb, maxc = map(int, input().split())
    mina, minb, minc = maxa, maxb, maxc
    for _ in range(n-1):
        da, db, dc = map(int, input().split())
        
        nmaxa = max(maxa, maxb) + da
        nmaxb = max(maxa, maxb, maxc) + db
        nmaxc = max(maxb, maxc) + dc
        
        nmina = min(mina, minb) + da
        nminb = min(mina, minb, minc) + db
        nminc = min(minb, minc) + dc
        
        maxa, maxb, maxc = nmaxa, nmaxb, nmaxc
        mina, minb, minc = nmina, nminb, nminc

    print(max(maxa, maxb, maxc), min(mina, minb, minc))

main()
