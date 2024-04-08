def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    if rows > cols:
        for i in range(rows):
            arr[i] += [0] * (rows - cols)
    elif cols > rows:
            arr += [[0] * cols] * (cols - rows)
    
    return arr