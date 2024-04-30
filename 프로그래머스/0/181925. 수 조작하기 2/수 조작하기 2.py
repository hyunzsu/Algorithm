def solution(numLog):
    d = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    res = ''
    for i in range(1, len(numLog)):
        res += d[numLog[i] - numLog[i-1]]
    return res