def solution(t, p):
    count = 0
    p_len = len(p)
    t_len = len(t)
    for i in range(t_len - p_len + 1):
        sub_str = t[i:i+p_len]
        if int(sub_str) <= int(p):
            count += 1 
    return count