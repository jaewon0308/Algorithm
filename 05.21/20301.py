from collections import deque
import sys
n,k,m = map(int,sys.stdin.readline().split())
queue = deque([i for i in range(1,n+1)])
count = 0

while queue:
    if count//m % 2 == 0:
        for i in range(k-1):
            queue.append(queue.popleft())
    else:
        for i in range(k):
            queue.appendleft(queue.pop())
    count += 1
    print(queue.popleft())