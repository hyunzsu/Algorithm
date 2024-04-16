def solution(s):
    if len(s) % 2 == 1:
        return s[(len(s) + 1) // 2 - 1]
    else:
        return s[(len(s) + 1) // 2 - 1:(len(s) + 1) // 2] + s[(len(s) + 1) // 2]