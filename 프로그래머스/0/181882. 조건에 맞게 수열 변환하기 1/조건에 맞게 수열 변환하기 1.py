def solution(arr):
    result = []
    for i in arr:
        if i % 2 != 0 and i < 50:
            result.append(i * 2)
        elif i % 2 == 0 and i >= 50: 
            result.append(i // 2)
        else:
            result.append(i)
    return result
            