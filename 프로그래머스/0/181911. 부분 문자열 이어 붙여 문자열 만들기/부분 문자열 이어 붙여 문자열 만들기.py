def solution(my_strings, parts):
    return ''.join(i[p[0]:p[1]+1] for i, p in zip(my_strings, parts))