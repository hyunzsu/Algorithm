def solution(n):
    res = ''
    for i in range(n):
        if i % 2 == 0:
            res += '수'
        else:
            res += '박'
    return res