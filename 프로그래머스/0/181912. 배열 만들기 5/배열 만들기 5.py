def solution(intStrs, k, s, l):
    result = []
    for str_num in intStrs:
        substring = str_num[s:s + l] 
        num = int(substring) 
        if num > k:
            result.append(num)
    return result