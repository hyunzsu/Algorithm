def solution(money):
    res = []
    for i in range(1):
        res.append(money // 5500)
        res.append(money - 5500 * (money // 5500))
    return res