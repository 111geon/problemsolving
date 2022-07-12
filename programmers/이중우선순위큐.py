import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        command, number = operation.split()
        if command == 'I':
            heapq.heappush(min_heap, int(number))
            heapq.heappush(max_heap, -int(number))
        else:
            if min_heap:
                if number == "-1":
                    del_num = heapq.heappop(min_heap)
                    max_heap.remove(-del_num)
                    heapq.heapify(max_heap)
                else:
                    del_num = -heapq.heappop(max_heap)
                    min_heap.remove(del_num)
                    heapq.heapify(min_heap)
    
    try:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    except:
        return [0, 0]
    