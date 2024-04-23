def solution(d, budget):
    d.sort()  # 부서별 신청 금액을 오름차순으로 정렬
    total = 0  # 현재까지 배정한 예산의 총액
    count = 0  # 지원한 부서의 수
    for amount in d:
        if total + amount <= budget:
            total += amount
            count += 1
        else:
            break
    return count