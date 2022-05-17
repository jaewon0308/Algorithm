x = int(input())
count = 1
stack = []
result = []
temp = True

for i in range(x):
    a = int(input())
    while count <= a:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == a:
        stack.pop()
        result.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in result:
        print(i)