def solution(my_string, is_suffix):
    suff = [my_string[i:] for i in range(len(my_string))]
    return 1 if is_suffix in suff else 0