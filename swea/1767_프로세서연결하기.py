def main():
    for t in range(1, int(input())+1):
        n = int(input())
        cores = []
        for _ in range(n):
            cores.append(list(map(int, input().split())))

        to_connect = []
        for i in range(1, n-1):
            for j in range(1, n-1):
                if cores[i][j] == 1: to_connect.append((i, j))

        max_connection = [0]
        min_wire = [2**63-1]
        solution(n, cores, 0, max_connection, to_connect, 0, min_wire)
        print("#" + str(t), min_wire[0])

def solution(n, cores, connection, max_connection, to_connect, wire, min_wire):
    directions = ["up", "down", "right", "left"]

    if not to_connect:
        if connection > max_connection[0]:
            min_wire[0] = wire
            max_connection[0] = connection
        if connection == max_connection[0]:
            min_wire[0] = min(min_wire[0], wire)
        return

    if connection + len(to_connect) < max_connection[0]:
        return

    if wire > min_wire[0] and connection + len(to_connect) == max_connection[0]:
        return
    
    peeked = to_connect[-1]
    for direction in directions:
        if peek_path(n, cores, peeked, direction):
            popped = to_connect.pop()
            wire += connect_path(n, cores, popped, direction, "connect")
            solution(n, cores, connection+1, max_connection, to_connect, wire, min_wire)
            wire -= connect_path(n, cores, popped, direction, "disconnect")
            to_connect.append(popped)
    popped = to_connect.pop()
    solution(n, cores, connection, max_connection, to_connect, wire, min_wire)
    to_connect.append(popped)

def peek_path(n, cores, core, direction):
    i, j = core
    connectable = True
    if direction == "up":
        while i > 0:
            i -= 1
            if cores[i][j] == 1: connectable = False
    if direction == "down":
        while i < n-1:
            i += 1
            if cores[i][j] == 1: connectable = False
    if direction == "right":
        while j < n-1:
            j += 1
            if cores[i][j] == 1: connectable = False
    if direction == "left":
        while j > 0:
            j -= 1
            if cores[i][j] == 1: connectable = False
    return connectable

def connect_path(n, cores, core, direction, connection):
    connection_map = {"connect": 1, "disconnect": 0}
    i, j = core
    wire = 0
    if direction == "up":
        while i > 0:
            i -= 1
            cores[i][j] = connection_map[connection]
            wire += 1
    if direction == "down":
        while i < n-1:
            i += 1
            cores[i][j] = connection_map[connection]
            wire += 1
    if direction == "right":
        while j < n-1:
            j += 1
            cores[i][j] = connection_map[connection]
            wire += 1
    if direction == "left":
        while j > 0:
            j -= 1
            cores[i][j] = connection_map[connection]
            wire += 1
    return wire
   
main()

'''
3  
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
9  
0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1
11 
0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 0 1 0 0
0 1 0 1 1 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
'''

'''
1
9
0 0 0 1 0 1 1 1 0
1 0 0 1 0 0 0 0 0
1 0 0 1 0 0 0 0 0
1 0 0 0 0 0 1 1 1
0 0 0 0 1 0 0 0 0
1 1 1 0 0 0 0 0 1
0 0 0 0 0 1 0 0 1
0 0 0 0 0 1 0 0 1
0 1 1 1 0 1 0 0 0
'''
