"""
서브태스크 문제였는데 50점맞았는데
그 이유가 시간초과였음
안알려줘서 시간 오래걸림
"""
import sys
from collections import deque
x = int(sys.stdin.readline())
queue = deque()

while 1:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    if n != 0 and len(queue) < x:
        queue.append(n)
    elif n == 0:
        queue.popleft()
if queue:
    print(*queue)
else:
    print('empty')