def solution(my_string):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    res = ''
    
    for s in my_string:
        if s not in aeiou:
            res += s
    return res
        