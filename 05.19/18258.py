import sys
from collections import deque
x = int(sys.stdin.readline())
queue = deque()

for i in range(x):
    n = sys.stdin.readline().split()

    if n[0] == 'push':
        queue.appendleft(n[1])
    elif n[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif n[0] == 'size':
        print(len(queue))
    elif n[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif n[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])