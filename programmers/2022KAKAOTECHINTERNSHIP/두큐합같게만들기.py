import collections

def solution(queue1, queue2):
    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    answer = 0
    max_ans = 2 * (len(queue1) + len(queue2))
    while answer < max_ans:
        if s1 > s2:
            popped = q1.popleft()
            s1 -= popped
            s2 += popped
            q2.append(popped)
        elif s2 > s1:
            popped = q2.popleft()
            s2 -= popped
            s1 += popped
            q1.append(popped)
        else:
            return answer
        answer += 1
    return -1

