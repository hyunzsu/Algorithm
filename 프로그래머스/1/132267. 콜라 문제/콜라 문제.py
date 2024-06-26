def solution(a, b, n):
    res = 0
    while n >= a: # 가지고 있는 콜라병이 교환 가능한 동안에
        res += (n // a * b) # 빈 병 개수 추가
        n = (n // a * b) + (n % a) # 교환하지 못하고 남은 병 + 새로 얻은 콜라
    return res