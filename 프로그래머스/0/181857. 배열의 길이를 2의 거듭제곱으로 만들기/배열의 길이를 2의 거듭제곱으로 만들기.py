def solution(arr):
    cnt = 1
    while cnt < len(arr):
        cnt *= 2
    # 필요한 0의 개수 계산 후 추가
    arr.extend([0] * (cnt - len(arr)))    
    return arr