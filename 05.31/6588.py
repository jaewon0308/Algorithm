"""
시간초과가 났다
1. 수정한 코드
2. 시간초과 코드

전체 범위내의 소수를 구할 줄 알아야 풀 수 있는 문제였다
에라토스테네스 체를 사용함
"""
#수정한 코드
import sys
R = 1000001
arr = [True for i in range(R+1)]

for i in range(2,int(R**0.5)+1):
    if arr[i] == True:
        j = 2
        while i * j <= R:
            arr[i*j] = False
            j += 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    result = 0
    for i in range(3,len(arr)):
        if arr[i] and arr[n-i]:
            result = n-i
            print(n,'=',i,'+',result)
            break

#시간초과가 난 코드
import sys
R = 1000001
arr = [True for i in range(R+1)]
stack = []
result = 0


for i in range(2,int(R**0.5)+1):
    if arr[i] == True:
        j = 2
        while i * j <= R:
            arr[i*j] = False
            j += 1
for i in range(2,R+1):
    if arr[i]:
        stack.append(i)


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in stack:
        if n-i in stack:
            result = n-i
            print(n,'=',i,'+',result)
            break