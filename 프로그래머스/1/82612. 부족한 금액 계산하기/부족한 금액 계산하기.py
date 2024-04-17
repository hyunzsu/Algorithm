def solution(price, money, count):
    total_cost = 0
    for i in range(1, count + 1):
        total_cost += (i * price)
    return max(0, total_cost - money)