def solution(arr1, arr2):
    res = []
    for i in range(len(arr1)): # 0 1
        row = []
        for j in range(len(arr1[i])): # 0 1 0 1
            row.append(arr1[i][j] + arr2[i][j])
        res.append(row)
    return res