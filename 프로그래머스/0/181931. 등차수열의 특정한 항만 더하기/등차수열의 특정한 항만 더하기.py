def solution(a, d, included):
    res = []
    for i, b in enumerate(included):
        if b:
            res.append(d * i + a)
    return sum(res)