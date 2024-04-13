def solution(x):
    st = list(str(x))
    count = 0
    for s in st:        
        count += int(s)
    return True if x % count == 0 else False
        