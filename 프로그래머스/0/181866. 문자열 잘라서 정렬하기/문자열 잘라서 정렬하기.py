def solution(myString):
    list = sorted(myString.split('x'))
    return [v for v in list if v]