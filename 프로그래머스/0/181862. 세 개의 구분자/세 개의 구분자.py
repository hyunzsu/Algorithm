def solution(myStr):
    split_str = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
    
    return split_str if split_str else ['EMPTY']