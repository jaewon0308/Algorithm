"""
구현은 쉬웠는데 문제 이해가 너무 오래걸렸음
문제 이해하는 능력을 길러야겠다!
"""

from collections import deque
n = int(input())
queue = list(map(int,input().split()))
result = deque()
queue.reverse()

for i in range(n):
    if queue[i] == 1:
        result.appendleft(i+1)
    elif queue[i] == 2:
        result.insert(1,i+1)
    elif queue[i] == 3:
        result.append(i+1)
print(*result)