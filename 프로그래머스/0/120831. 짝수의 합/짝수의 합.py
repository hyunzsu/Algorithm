def solution(n):
    res = 0
    for i in range(0, n+1, 2):
        res = res + i
    return res