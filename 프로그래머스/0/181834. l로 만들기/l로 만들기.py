def solution(myString):
    res = ""
    for s in myString:
        if s < 'l':
            res += 'l'
        else:
            res += s
    return res