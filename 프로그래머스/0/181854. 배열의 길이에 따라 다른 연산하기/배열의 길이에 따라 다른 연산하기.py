def solution(arr, n):
    odd_res = []
    even_res = []
    for i in range(len(arr)):
        if i % 2 == 0:
            odd_res.append(arr[i] + n)
            even_res.append(arr[i])
        else:
            odd_res.append(arr[i])
            even_res.append(arr[i] + n)
    return odd_res if len(arr) % 2 != 0 else even_res
    