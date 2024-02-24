def solution(num_list):
    res = 0
    if len(num_list) >= 11:
        res = sum(num_list)
    else:
        res = 1
        for num in num_list:
            res *= num
    return res