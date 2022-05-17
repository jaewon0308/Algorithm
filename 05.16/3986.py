a = int(input())
result = 0
for i in range(a):
    b = input().strip()
    stack = []
    for j in b:
        if len(stack) == 0:
            stack.append(j)
        else:
            if j == stack[-1]:
                stack.pop()
            else:
                stack.append(j)
    if len(stack) == 0:
        result += 1
print(result)