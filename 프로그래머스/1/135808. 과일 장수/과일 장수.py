def solution(k, m, score):
    res = 0
    apple = sorted(score, reverse=True)
    for i in range(0, len(apple), m):
        if i + m > len(apple):
            break
        res += apple[i+m-1] * m
    return res