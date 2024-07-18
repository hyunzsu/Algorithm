import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())  # 수 입력 받기
    cnt = 0
    i = 5
    while i <= n:
        cnt += n // i  # 5의 배수의 합을 구한다
        i *= 5
    print(cnt)