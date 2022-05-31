"""
1. for문으로 구현
2. 재귀함수로 구현
3. math.factorial로 구현
"""
#for문으로 구현
n = int(input())
result = 1
for i in range(1,n+1):
    result = i * result
print(result)

#재귀함수로 구현
def fac(n):
    if n > 1:
        return n * fac(n-1)
    else:
        return 1

print(fac(int(input())))

#math.factorial로 구현
import math

n = int(input())
print(math.factorial(n))