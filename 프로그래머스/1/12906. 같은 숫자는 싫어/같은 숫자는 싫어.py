def solution(arr):
    res = []
    for num in arr:
        if not res or num != res[-1]:
            res.append(num)
    return res