def solution(n):
    # 3진법으로 변환
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return int(ternary[::-1], 3)