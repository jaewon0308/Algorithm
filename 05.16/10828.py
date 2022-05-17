x = int(input())
q = []
answer =[]
for i in range(x):
    a = list(input().split())
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'pop':
        if q:
            answer.append(q.pop())
        else:
            answer.append('-1')
    elif a[0] == 'size':
        answer.append(len(q))
    elif a[0] == 'top':
        if q:
            answer.append(q[-1])
        else:
            answer.append('-1')
    elif a[0] == 'empty':
        if len(q) == 0:
            answer.append('1')
        else:
            answer.append('0')
for i in answer:
    print(i)