def solution(myString, pat):
    change = ''.join(['B' if char == 'A' else 'A' if char == 'B' else char for char in myString])
    
    return 1 if pat in change else 0