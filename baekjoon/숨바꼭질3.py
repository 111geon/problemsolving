import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    print(solution(n, k))
   
def solution(n, k):
    if n >= k: return n - k
    if k % 2 == 0 and abs(k//2 - n) <= k - n:
        return solution(n, k//2)

    level = 0
    q = [n]
    v = set(q)
    teleport(q, k, v)
   
    while k not in v:
        temp = []
        for qq in q:
            qq1, qq2 = qq - 1, qq + 1
            
            if qq1 not in v and qq1 >= 0 :
                v.add(qq1)
                temp.append(qq1)
                teleport(temp, k, v)                

            if qq2 not in v and qq2 <= k * 3 //2:
                v.add(qq2)
                temp.append(qq2)
                teleport(temp, k, v)
   
        q = temp[:]     
        level += 1
        
    return level

def teleport(q, k, v):
    while True:
        peek = 2 * q[-1]
        if peek >= k * 3 // 2 or not peek: return
        v.add(peek)
        q.append(peek)    

main()

"""
(i) 우선 n이 k보다 큰 경우에는 -1 씩 걸어가는 수밖에 없다.
(ii) 2배 순간이동은 no cost이므로 n이 짝수인 경우 반을 나눠준 n//2을 목적지로 한다.
    - 기존 목적지 n과 새 목적지 n//2 중 누가 더 유리한지 판단해주어야 한다.
    - 더 가까운 쪽이 더 유리하다.
(iii) 목적지가 정해지면 0-1 BFS 진행
    - temp 리스트에 q에 순간이동한 점들을 추가하면서 visit
        - 증가한 위치의 상한선은 k * 3 // 2로 설정했는데 이는 이를 넘으면 무조건 
          기존위치보다 멀어지기 때문에
    - q를 temp로 갱신해줌
    - 이후에 해당 점들로 부터 걷는 작업을 하면서 level 증가.
"""
