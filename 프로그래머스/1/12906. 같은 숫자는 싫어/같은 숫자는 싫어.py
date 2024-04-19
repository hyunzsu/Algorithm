def solution(arr):
    res = []
    for i in arr:
        if res[-1:] == [i]: 
            continue
        res.append(i)
    return res