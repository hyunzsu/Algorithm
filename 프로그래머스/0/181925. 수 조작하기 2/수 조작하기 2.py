def solution(numLog):
    result = ""
    for i in range(len(numLog)):
        diff = numLog[i] - (numLog[i - 1] if i > 0 else 0)

        if diff == 1:
            result += "w"
        elif diff == -1:
            result += "s"
        elif diff == 10:
            result += "d"
        elif diff == -10:
            result += "a"

    return result