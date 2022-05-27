"""
Count 사용법 숙지!
"""
from collections import Counter
n = int(input())
a = list(map(int,input().split()))
count = Counter(a)
stack = [0]
result = [-1] * n

for i in range(n):
    while stack and count[a[stack[-1]]] < count[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)