def solution(a, b):
    r = str(a) + str(b)
    return max(int(r), 2 * a * b)