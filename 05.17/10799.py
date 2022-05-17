x = list(input())
stack = []
result = 0
for i in range(len(x)):
    if x[i] == '(':
        stack.append('(')
    else:
        if x[i-1] == ')':
            stack.pop()
            result += 1
        else:
            stack.pop()
            result += len(stack)
print(result)