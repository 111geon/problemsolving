def main():
    t = int(input())
    for tt in range(1, t+1):
        n, k = map(int, input().split())
        print("#" + str(tt) + " " + solution(n, k))

def solution(n, k):
    ans = 0
    rows = []
    cols = ['0' for _ in range(n)]
    for _ in range(n):
        row = "".join(input().split())
        rows.append('0' + row + '0')
        for i in range(n):
            cols[i] += row[i]
    for i in range(n):
        cols[i] += '0'

    for row in rows:
        ans += findall('0'+'1'*k+'0', row)
    for col in cols:
        ans += findall('0'+'1'*k+'0', col)

    return str(ans)

def findall(pat, string):
    result = 0
    for i in range(len(string)-len(pat)+1):
        if string[i:i+len(pat)] == pat: result += 1
    return result

main()
