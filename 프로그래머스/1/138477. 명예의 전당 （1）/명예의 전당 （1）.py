def solution(k, score):
    tmp = []
    res = []
    for i in range(1, len(score)+1): 
        tmp.append(score[:i])
    for t in tmp:
        # print(sorted(t, reverse=True)[:k])
        res.append(min(sorted(t, reverse=True)[:k]))
    return res
    