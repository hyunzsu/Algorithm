def solution(my_string):
    alphabet = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    
    count_list = []
    for letter in alphabet:
        count_list.append(my_string.count(letter))
    
    return count_list
