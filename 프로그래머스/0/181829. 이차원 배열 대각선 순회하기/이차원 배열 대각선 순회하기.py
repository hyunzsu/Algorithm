def solution(board, k):
    res = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                res.append(board[i][j])
    return sum(res)