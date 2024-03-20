from itertools import permutations
import re

def operation(n1, n2, op):
    if op == '+':
        return str(int(n1) + int(n2))
    elif op == '-':
        return str(int(n1) - int(n2))
    elif op == '*':
        return str(int(n1) * int(n2))

def calculate(expression, ops):
    arr = re.findall(r'\d+|\D', expression)
    for op in ops:
        stack = []
        while len(arr) > 0:
            temp = arr.pop(0)
            if temp == op:
                stack.append(operation(stack.pop(), arr.pop(0), op))
            else:
                stack.append(temp)
        arr = stack
    return abs(int(arr[0]))

def solution(expression):
    operators = ['+', '-', '*']
    max_value = 0
    for ops in permutations(operators, 3):
        max_value = max(max_value, calculate(expression, ops))
    return max_value