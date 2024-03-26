def solution(rank, attendance):
    available = [(r, i) for i, (r, a) in enumerate(zip(rank, attendance)) if a]
    
    available.sort()

    selected = [student[1] for student in available[:3]]
    
    result = 10000 * selected[0] + 100 * selected[1] + selected[2]
    return result