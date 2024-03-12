def solution(strArr):
    res = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            res.append(strArr[i].lower())
        else:
            res.append(strArr[i].upper())
    return res