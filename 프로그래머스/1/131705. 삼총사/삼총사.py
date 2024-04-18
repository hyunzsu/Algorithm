import itertools

def solution(number):
    a = itertools.combinations(number, 3)
    res = 0
    for s in list(a):
        if sum(s) == 0:
            res += 1  
    return res