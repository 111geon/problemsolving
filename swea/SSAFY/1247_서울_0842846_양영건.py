def main():
    for t in range(1, int(input())+1):
        n = int(input())
        xys = list(map(int, input().split()))
        start = (xys[0], xys[1])
        end = (xys[2], xys[3])
        clients = []
        for i in range(n):
            clients.append((xys[4+2*i], xys[5+2*i]))

        min_score = [2**63-1]
        solution(start, end, clients, 0, min_score)
        print("#" + str(t), min_score[0])

def solution(start, end, clients, score, min_score):
    if score >= min_score[0]: return
    if not clients: 
        min_score[0] = min(min_score[0], score + abs(start[0]-end[0]) + abs(start[1]-end[1]))
        return
    for i in range(len(clients)):
        client = clients[i]
        next_score = score + abs(client[0]-start[0]) + abs(client[1]-start[1])
        solution(client, end, clients[:i]+clients[i+1:], next_score, min_score)
        
main()

'''
2
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
6
88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14
'''
