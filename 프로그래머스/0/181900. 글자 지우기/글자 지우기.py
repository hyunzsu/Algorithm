def solution(my_string, indices):
    string = list(my_string)
    indices.sort(reverse=True)
    for index in indices:
        del string[index]
    return ''.join(string)