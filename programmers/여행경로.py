from collections import defaultdict

def solution(tickets):
    to_visit = defaultdict(list)
    for ticket in tickets:
        to_visit[ticket[0]].append(ticket[1])
    for k, v in to_visit.items():
        v.sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    
    while stack:
        _next = to_visit[stack[-1]]
        if _next:
            stack.append(_next.pop())
        else:
            path.append(stack.pop())
    
    return path[::-1]