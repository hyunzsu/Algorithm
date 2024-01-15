def solution(a, b):
    a = str(a)
    b = str(b)
    answer = max((a + b), (b + a))
    return int(answer)