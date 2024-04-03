def solution(str_list, ex):
    res = []
    for s in str_list:
        if ex not in s:
            res.append(s)
    return ''.join(res)