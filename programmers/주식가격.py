def solution(prices):
    answer = [0 for _ in range(len(prices))]
    prices = list(zip(range(len(prices)), prices))
    prices.append((len(prices)-1, 0))
    stack = []
    for price in prices:
        while(stack and price[1] < stack[-1][1]):
            s = stack.pop()
            answer[s[0]] = price[0] - s[0]
        stack.append(price)
            
    return answer

def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
