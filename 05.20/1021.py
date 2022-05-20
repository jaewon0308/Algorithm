"""
원형큐처럼 쓰고 싶으면 굳이 pop할 필요없이 rotate 메소드를 사용하면 된다
"""
from collections import deque

n,m = map(int,input().split())
a = list(map(int,input().split()))
queue = deque([i for i in range(1,int(n)+1)])
result = 0

for i in a:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2 :
                while queue[0] != i:
                    queue.rotate(-1)
                    result += 1
            else:
                while queue[0] != i:
                    queue.rotate(1)
                    result += 1
print(result)