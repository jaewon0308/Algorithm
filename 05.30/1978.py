"""
소수의 특징
1. 2보다 크거나 같다.
2. N-1보다 작거나 같은 자연수로 나누어떨어지면 안된다.
"""
n = int(input())
num = map(int,input().split())
result = 0
for i in num:
    non_result = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                non_result += 1
        if non_result == 0:
            result += 1
print(result)