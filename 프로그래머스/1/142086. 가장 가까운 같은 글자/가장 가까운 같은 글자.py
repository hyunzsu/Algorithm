def solution(s):
    res = []
    d = {} # 문자의 마지막 등장 위치 저장
    for i, ss in enumerate(s):
        if ss in d:
            distance = i - d[ss]
            res.append(distance)
        else:
            res.append(-1)
        d[ss] = i
        # print(d)
    return res