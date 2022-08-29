MAX_INT = 2**63-1
DX = [-1, 1, 0, 0]
DY = [0, 0, 1, -1]

def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        cores = []
        for _ in range(n): cores.append(list(map(int, input().split())))

        to_conn = []
        for i in range(1, n-1):
            for j in range(1, n-1):
                if cores[i][j] == 1: to_conn.append((i, j))

        max_conn = [0]
        min_wire = [MAX_INT]
        dfs(n, cores, to_conn, 0, max_conn, 0, min_wire)
        print("#" + str(t), min_wire[0])

def dfs(n, cores, to_conn, conn, max_conn, wire, min_wire):
    if not to_conn:
        if conn > max_conn[0]:
            min_wire[0] = wire
            max_conn[0] = conn
        if conn == max_conn[0]:
            min_wire[0] = min(min_wire[0], wire)
        return

    if conn + len(to_conn) < max_conn[0]: return
    if wire > min_wire[0] and conn + len(to_conn) == max_conn[0]: return
    
    peeked = to_conn[-1]
    for d in range(4):
        if is_connectable(n, cores, peeked, d):
            popped = to_conn.pop()
            wire += connect(n, cores, popped, d, 1)
            dfs(n, cores, to_conn, conn+1, max_conn, wire, min_wire)
            wire -= connect(n, cores, popped, d, 0)
            to_conn.append(popped)
    popped = to_conn.pop()
    dfs(n, cores, to_conn, conn, max_conn, wire, min_wire)
    to_conn.append(popped)

def is_connectable(n, cores, core, d):
    x, y = core
    while True:
        x += DX[d]
        y += DY[d]
        if x < 0 or y < 0 or x >= n or y >= n: return True
        if cores[x][y] == 1: return False

def connect(n, cores, core, d, connect):
    x, y = core
    wire = 0
    while True:
        x += DX[d]
        y += DY[d]
        if x < 0 or y < 0 or x >= n or y >= n: return wire
        cores[x][y] = connect
        wire += 1
        
if __name__ == "__main__":
    main()
