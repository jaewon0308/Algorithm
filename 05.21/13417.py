"""
쉬웠는데 문제 이해를 처음에 잘못해서 오래걸렸음
문제 이해능력을 기르자!
"""
from collections import deque

for i in range(int(input())):
    n = int(input())
    queue = deque(input().split())
    result = deque(queue.popleft())
    while queue:
        x = queue.popleft()
        if x > result[0]:
            result.append(x)
        else:
            result.appendleft(x)
    print(*result,sep='')