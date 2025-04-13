def solution(sides):
    sorted_list = sorted(sides)
    return 2 if sorted_list[2] >= sorted_list[0] + sorted_list[1] else 1