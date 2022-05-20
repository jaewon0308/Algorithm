from collections import deque
n = int(input())
queue = deque(enumerate(map(int,input().split())))
result = []

while queue:
    num, mes = queue.popleft()
    result.append(num+1)

    if mes > 0:
        queue.rotate(-(mes-1))
    else:
        queue.rotate(-mes)

print(*result)