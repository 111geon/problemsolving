def main():
    t = int(input())
    for tt in range(1, t+1):
        print("#" + str(tt), solution())

def solution():
    rows = []
    cols = [[] for _ in range(9)]
    for _ in range(9):
        row = input().split()
        rows.append(row)

        for i in range(9):
            cols[i].append(row[i])

    for row in rows:
        if len(row) != len(set(row)):
            return '0'
    
    for col in cols:
        if len(col) != len(set(col)):
            return '0'

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for k in range(3):
                for l in range(3):
                    square.append(cols[i+k][j+l])
            if len(square) != len(set(square)):
                return '0'

    return '1'

main()
