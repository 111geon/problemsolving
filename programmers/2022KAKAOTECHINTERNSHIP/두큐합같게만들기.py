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

"""
- greedy
- 그리디하게 합이 큰 쪽의 큐에서 pop하여 합이 작은 쪽의 큐에 append한다.
- 그리디한 해가 유일해는 아니나 해에 속한다.
    - 어떤 해에서도 결국 큰 쪽에서 pop하여 작은 쪽에 append하는 동작이 있기 때문에?
- 두 큐를 각각 2번씩 순회하는 것이 동작 수의 upper bound이다.
"""
