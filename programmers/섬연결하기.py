def solution(n, costs):
    answer = 0
    if n == 1:
        return answer
    costs.sort(key=lambda x: x[2], reverse=True)
    bridge = costs.pop()
    group = set((bridge[0], bridge[1]))
    answer += bridge[2]
    while len(group) < n:
        i = len(costs) - 1
        while i >= 0:
            if costs[i][0] in group and costs[i][1] in group:
                pass
            elif costs[i][0] in group or costs[i][1] in group:
                bridge = costs.pop(i)
                group.update((bridge[0], bridge[1]))
                answer += bridge[2]
                break
            i -= 1
    return answer
