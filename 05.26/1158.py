from collections import deque
num = list(input().split())
queue = deque([i for i in range(1,int(num[0])+1)])
result = []
while queue:
    for i in range(int(num[1])-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
#출력방법 1 
print('<', ', '.join(str(i) for i in result), '>',sep='')
#출력방법 2
print('<',end='')
print(*result,sep=', ',end='')
print('>')