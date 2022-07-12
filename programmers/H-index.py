def solution(citations):
    citations.sort(reverse=True)
    for n in range(1, len(citations)+1):
        if n > citations[n-1]:
            return n-1
    else:
        return n
