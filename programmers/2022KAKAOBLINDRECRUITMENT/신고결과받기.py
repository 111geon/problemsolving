import collections

def solution(id_list, report, k):
    reports = collections.defaultdict(set)
    report = set(report)
    reported = collections.defaultdict(int)
    for r in report:
        a, b = r.split()
        reports[a].add(b)
        reported[b] += 1
    
    banned = set()
    for user, num in reported.items():
        if num >= k: banned.add(user)
    
    answer = []
    for user in id_list:
        answer.append(len(banned.intersection(reports[user])))
    
    return answer

"""
- Set
- reports[i] -> set() : reports는 i라는 사람이 신고한 사용자들의 set을 담는다.
- report를 set(report)하여 중복된 신고를 걸러준다.
- reported[i] -> int : reported는 i라는 사람이 받은 신고수 int를 담는다.
- banned: 신고를 k번 이상 당해 정지당한 사용자의 set.
"""
