def solution(s):
    res = []
    ss = s.split(' ')
    for r in ss:
        word = []
        for i in range(len(r)):
            if i % 2 == 0:
                word.append(r[i].upper())
            else:
                word.append(r[i].lower())
        res.append(''.join(word))
    return ' '.join(res)