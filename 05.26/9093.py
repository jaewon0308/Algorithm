"""
인덱스 슬라이싱으로 풀이
"""
import sys

n = int(input())
for _ in range(n):
    x = sys.stdin.readline().split()
    stack = []
    for i in x:
        stack.append(i[::-1])
    print(*stack)


"""
reverse로 풀이
"""
import sys

n = int(input())
x = [list(sys.stdin.readline().split())for i in range(n)]

for _ in range(n):
    for i in x[_]:
        print(''.join(reversed(list(i))),end=' ')
    print()
