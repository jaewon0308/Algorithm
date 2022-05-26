n = int(input())

for _ in range(n):
    x = input()
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')