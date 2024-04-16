def solution(n):
    num = n - 1
    for i in range(2, num+1):
        if num % i == 0:
            result = i
            break
    return result