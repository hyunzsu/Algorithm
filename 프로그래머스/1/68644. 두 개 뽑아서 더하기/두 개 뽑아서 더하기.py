from itertools import combinations

def solution(numbers):
    res = []
    l = list(combinations(numbers, 2))
    for s in l:
        res.append(sum(s))
    return sorted(set(res))