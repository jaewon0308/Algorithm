while 1:
    x = input()
    stack = []
    if x == '.':
        break

    for i in range(len(x)):
        if x[i] == '(' or x[i] == '[':
            stack.append(x[i])
        elif x[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif x[i] == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')