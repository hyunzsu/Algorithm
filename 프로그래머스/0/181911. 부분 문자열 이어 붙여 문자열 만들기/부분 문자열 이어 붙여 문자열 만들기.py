def solution(my_strings, parts):
    res = []
    for i, p in zip(my_strings, parts):
        res.append(i[p[0]:p[1]+1])
    return ''.join(res)