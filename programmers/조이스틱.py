# def solution(name):
#     answer = 0

#     updowns = dict()
#     for letter in "ABCDEFGHIJKLMN": updowns[letter] = ord(letter) - 65
#     for letter in "OPQRSTUVWXYZ": updowns[letter] = -(ord(letter) - 65) + 26
#     for n in name: answer += updowns[n]
    
#     forward = name[:]
#     backward = name[0] + name[-1:0:-1]
#     cand = [forward, backward]
    
#     if len(name) == 1: return answer
    
#     for s in (forward, backward):
#         for i in range(1, len(name)//2):
#             if s[i] != 'A' and s[i+1] == 'A':
#                 cand.append(s[:i+1] + s[i-1::-1] + s[-1:i-len(s):-1])
    
#     leftrights = float('inf')
#     for c in cand:
#         while(c[-1] == 'A' and len(c) > 1): c = c[:-1]
#         leftrights = min(leftrights, len(c) - 1)
#     answer += leftrights
    
#     return answer

# BABBBAAAAAAABBAA
# 앞은 B고 뒤는 A일때, 절반을 안넘어갔을 때,

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer
