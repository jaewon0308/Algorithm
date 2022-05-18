
stack으로 풀었을 때 시간초과가 나서 deque로 풀게 됨

from collections import deque

x = int(input())
deque = deque([i for i in range(1, x+1)])

while len(deque)  1
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
print(deque[0])