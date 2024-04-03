def solution(arr, delete_list):
    res = list(set(arr) - set(delete_list))
    res.sort(key = arr.index)
    return res
                