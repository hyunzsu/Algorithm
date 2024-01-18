def solution(num_list):
    odd_sum = int(''.join(str(num) for num in num_list if num % 2 != 0))
    even_sum = int(''.join(str(num) for num in num_list if num % 2 == 0))
    
    return odd_sum + even_sum