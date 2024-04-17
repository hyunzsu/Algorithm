def solution(a, b):
    res = 0
    for pair in zip(a, b):
        res += (pair[0] * pair[1])
    return res