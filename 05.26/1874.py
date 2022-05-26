n = int(input())
stack = []
result = []
count = 1
temp = True
for i in range(n):
    x = int(input())
    while count <= x:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    print(*result,sep='\n')