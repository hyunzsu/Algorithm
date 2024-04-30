def solution(n, arr1, arr2):
    res = []
    for a1, a2 in zip(arr1, arr2):
        # 이진수로 변환하고 자릿수를 맞춤
        a1_bin = bin(a1)[2:].zfill(n)
        a2_bin = bin(a2)[2:].zfill(n)
        print(a1_bin, a2_bin)
        # 두 지도를 비교하여 최종 지도 생성
        row = ''
        for i in range(n):
            if a1_bin[i] == '1' or a2_bin[i] == '1':
                row += '#'
            else:
                row += ' '
        res.append(row)
    return res