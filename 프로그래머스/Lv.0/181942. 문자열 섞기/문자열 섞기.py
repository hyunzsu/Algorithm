def solution(str1, str2):
    result = ''
    
    for str1, str2 in zip(str1, str2):
        result += str1 + str2

    return result