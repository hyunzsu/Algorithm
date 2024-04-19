def solution(left, right):
    res = 0
    for i in range(left, right+1): # 13, 14, 15, 16, 17
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            res += i
        else:
            res -= i
    return res