def solution(n):
    # 2차원 배열 초기화
    res = [[0] * n for _ in range(n)]
    
    # 초기 위치 및 값 설정
    value = 1
    row, col = 0, 0
    direction = 0
    
    # 시계 방향 나선형으로 값 배치
    while value <= n * n:
        res[row][col] = value
        
        # 다음 위치 계산
        if direction == 0:  # 오른쪽
            col += 1
            if col == n or res[row][col] != 0:
                col -= 1
                row += 1
                direction = 1
        elif direction == 1:  # 아래쪽
            row += 1
            if row == n or res[row][col] != 0:
                row -= 1
                col -= 1
                direction = 2
        elif direction == 2:  # 왼쪽
            col -= 1
            if col < 0 or res[row][col] != 0:
                col += 1
                row -= 1
                direction = 3
        else:  # 위쪽
            row -= 1
            if row < 0 or res[row][col] != 0:
                row += 1
                col += 1
                direction = 0
        
        value += 1
    
    return res