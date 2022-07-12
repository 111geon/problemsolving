import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    
    count = 0
    while(len(scoville) > 0):
        min_1 = hq.heappop(scoville)
        
        if min_1 >= K:
            break
        
        if len(scoville) == 0:
            return -1
        
        min_2 = hq.heappop(scoville)
        hq.heappush(scoville, min_1 + min_2 * 2)
        count += 1
        
    return count
