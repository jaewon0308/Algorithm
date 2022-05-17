"""
소요시간 15분
"""
import sys

x = int(sys.stdin.readline())
stack = []
result = 1

for i in range(x):
    stack.append(int(sys.stdin.readline()))
max_point = stack[-1]

for i in range(x):
    if max_point < stack[x-i-1]:
        result += 1
        max_point = stack[x-i-1]
print(result)