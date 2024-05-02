def solution(name, yearning, photo):
    d = dict(zip(name, yearning)) # {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}
    res = []
    for p in photo:
        cnt = 0
        for j in p:
            if j in d:
                cnt += d[j]
            else:
                cnt += 0
        res.append(cnt)
    return res