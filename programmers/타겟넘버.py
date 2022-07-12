def solution(numbers, target):
    answer = 0
    for added in stack_adds(numbers):
        answer += 1 if added == target else 0
    return answer

def stack_adds(numbers):
    if len(numbers) == 1:
        return [numbers[0], -numbers[0]]
    sub_stack = stack_adds(numbers[1:])
    pos_stack = []
    neg_stack = []
    for a in sub_stack:
        pos_stack.append(a + numbers[0])
        neg_stack.append(a - numbers[0])
    return pos_stack + neg_stack

# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
