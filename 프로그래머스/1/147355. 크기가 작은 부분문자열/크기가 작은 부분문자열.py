def solution(t, p):
    p_length = len(list(p))
    t_slice = list(map(int, t)) # [3, 1, 4, 1, 5, 9, 2]
    # print(t_slice[:3])
    for tt in t:
        print(tt)