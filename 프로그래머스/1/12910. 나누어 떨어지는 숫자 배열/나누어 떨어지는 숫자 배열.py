def solution(arr, divisor):
    res = []
    for a in arr:
        if a % divisor == 0:
            res.append(a)
    if res == []:
        return [-1]
    return sorted(res) 