def solution(n):
    res = 0
    for s in str(n):
        res += int(s)
    return res