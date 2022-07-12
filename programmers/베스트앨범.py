def solution(genres, plays):
    answer = []
    
    genres_ids = dict()
    for i, g, p in zip(range(len(genres)), genres, plays):
        if g in genres_ids:
            if p > genres_ids[genres[i]][0][1]:
                genres_ids[g][1] = genres_ids[g][0]
                genres_ids[g][0] = (i, p)
            elif p > genres_ids[g][1][1]:
                genres_ids[g][1] = (i, p)
            genres_ids[g][2] += p
        else:
            genres_ids[g] = [(i, p), (-1, 0), p]
    
    for x in sorted(genres_ids.items(), key=lambda x: x[1][2], reverse=True):
        for i in x[1][:2]:
            if i[0] != -1: answer.append(i[0])
    
    return answer
