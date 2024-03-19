def solution(myString):
    # print(myString.split('x'))
    spl = myString.split('x')
    return list(map(lambda x: len(x), spl))