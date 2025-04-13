def solution(s1, s2):
    res = 0
    for s in s2:
        if s in s1:
            res += 1
    return res