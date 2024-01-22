def solution(num_list):
    if len(num_list) < 2:
        return num_list
    
    last_element = num_list[-1]
    second_last_element = num_list[-2]

    if last_element > second_last_element:
        difference = last_element - second_last_element
        num_list.append(difference)
    else:
        num_list.append(last_element * 2)

    return num_list
    
