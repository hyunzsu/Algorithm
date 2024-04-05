def solution(picture, k):
    res = []
    for row in picture:
        resized = ''
        for pixel in row:
            resized += pixel * k
        for _ in range(k):
            res.append(resized)
    return res