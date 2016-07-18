def calc(expression):
    elements = expression.split(' ')
    stack = []
    for ele in elements:
        if ele == '+':
            para2 = stack.pop()
            para1 = stack.pop()
            stack.append(para1 + para2)
        elif ele == '-':
            para2 = stack.pop()
            para1 = stack.pop()
            stack.append(para1 - para2)
        elif ele == '*':
            para2 = stack.pop()
            para1 = stack.pop()
            stack.append(para1 * para2)
        elif ele == '/':
            para2 = stack.pop()
            para1 = stack.pop()
            stack.append(para1 / para2)
        else:
            stack.append(int(ele))
    print stack.pop()


calc('7 8 + 3 2 + /')
calc('5 1 2 + 4 * + 3 -')
calc('1 2 3 + -')
