def solution(n):
    if int(n**0.5) == n**0.5: # 제곱수 판별
        return ((n**0.5)+1)**2 
    else : 
        return -1 