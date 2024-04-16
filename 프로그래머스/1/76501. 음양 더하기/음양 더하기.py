def solution(absolutes, signs):
    a = 0
    b = 0
    for pair in zip(absolutes, signs):
        if pair[1]:
            a += pair[0]
        if pair[1] == False:
            b += -pair[0]
    return a + b