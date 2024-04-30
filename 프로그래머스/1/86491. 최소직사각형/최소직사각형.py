def solution(sizes):
    w = []
    h = []
    for size in sizes:
        width, height = max(size), min(size)
        w.append(width)
        h.append(height)
    return max(w) * max(h)