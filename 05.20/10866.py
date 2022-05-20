from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    x = sys.stdin.readline().split()

    if x[0] == 'push_front':
        queue.appendleft(x[1])
    elif x[0] == 'push_back':
        queue.append(x[1])
    elif x[0] == 'pop_front':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print('-1')
    elif x[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print('-1')
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif x[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    elif x[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print('-1')
