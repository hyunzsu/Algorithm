def solution(my_string, indices):
    modified_string = ''.join([char for index, char in enumerate(my_string) if index not in indices])
    return modified_string