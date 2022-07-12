import heapq as hq
import sys

def solution(jobs):
    num_jobs = len(jobs)
    jobs = sorted(jobs, reverse=True)
    
    answer = 0
    waiting = []
    job = jobs.pop()
    t = job[0]
    
    jobs = [[sys.maxsize, 0], [sys.maxsize, 0]] + jobs
    
    while(jobs):
        if job[0] < t:
            hq.heappush(waiting, (job[1], job[0]))
            job = jobs.pop()
            
        else:
            if not waiting:
                answer += job[1]
                t = job[0] + job[1]
                job = jobs.pop()
                
            else:
                subjob = hq.heappop(waiting)
                answer += t - subjob[1] + subjob[0]
                t += subjob[0]

    return answer // num_jobs


# import heapq
# from collections import deque

# def solution(jobs):
#     tasks = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]), reverse=True)
#     q = []
#     heapq.heappush(q, tasks.pop())
#     current_time, total_response_time = 0, 0
#     while len(q) > 0:
#         dur, arr = heapq.heappop(q)
#         current_time = max(current_time + dur, arr + dur)
#         total_response_time += current_time - arr
#         while len(tasks) > 0 and tasks[-1][1] <= current_time:
#             heapq.heappush(q, tasks.pop())
#         if len(tasks) > 0 and len(q) == 0:
#             heapq.heappush(q, tasks.pop())
#     return total_response_time // len(jobs)
