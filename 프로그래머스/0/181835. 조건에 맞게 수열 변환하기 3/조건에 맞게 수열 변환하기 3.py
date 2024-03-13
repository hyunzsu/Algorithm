def solution(arr, k):
    res = []
    for i in arr:
        if k % 2 != 0:
            res.append(i * k)
        else:
            res.append(i + k)
    return res
        