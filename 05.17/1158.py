from collections import deque

x,y = map(int,input().split())
q = deque([])

for i in range(1,x+1):
    q.append(i)
print('<',end='')
while q:
    for i in range(y-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(),end='')
    if q:
        print(',',end=' ')
print('>')