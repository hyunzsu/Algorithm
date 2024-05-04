def solution(array, commands):
    res = []
    for c in commands: 
        s = array[c[0]-1:c[1]] 
        s.sort()
        res.append(s[c[2]-1])
    return res
        