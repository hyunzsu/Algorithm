def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk: # stk 빈배열
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop() # stk 마지막 원소 제거
        else: # stk 마지막 원소가 arr[i]와 다르면
            stk.append(arr[i])
        i += 1
    return stk if stk else [-1]