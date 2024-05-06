def solution(nums):
    unique = set(nums)  # 중복을 제거한 폰켓몬 종류 집합
    max_res = min(len(unique), len(nums) // 2)  # 선택할 수 있는 최대 폰켓몬 종류 수
    return max_res