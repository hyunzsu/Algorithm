def solution(order):
    res = 0
    for s in order:
        if s == "anything" or "americano" in s:
            res += 4500
        elif "cafelatte" in s:
            res += 5000 
    return res