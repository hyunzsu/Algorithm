def solution(food):
    res = '' 
    for i in range(1, len(food)): # 1 2 3
        res += (food[i] // 2) * str(i)
        print(res)
    return res + '0' + res[::-1]