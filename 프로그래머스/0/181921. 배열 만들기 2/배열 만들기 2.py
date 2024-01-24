def solution(l, r):
    result = []
    for num in range(l, r + 1):
        if set(str(num)) <= {'0', '5'}:
            result.append(num)

    return result if result else [-1]