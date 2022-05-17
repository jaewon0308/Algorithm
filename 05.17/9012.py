x = int(input())
for _ in range(x):
    count = 0
    y = input()
    start = list(y)
    for i in y:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            print('NO')
            break
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')