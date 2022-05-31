"""
2번 코드로 풀면 시간초과가 나서
저번에 풀지 않았던 방법인
2와 5의 배수를 찾는 것으로 했다
이건 조합이기 때문에 2, 5의 배수 중
어떤 수가 작은지 알 수 없기 때문에
min을 통해 계산해줬다

1. 2, 5의 배수를 찾아 작은 것으로 구하기
2. 인덱스 슬라이싱(시간초과)
"""
#2, 5의 배수를 찾아 작은 것으로 구하기
n,m = map(int,input().split())

def twoCount(n):
    two = 0
    while n != 0:
        n = n //2
        two += n
    return two
def fiveCount(n):
    five = 0
    while n != 0:
        n = n //5
        five += n
    return five

print(min(twoCount(n)-twoCount(n-m)-twoCount(m),fiveCount(n)-fiveCount(n-m)-fiveCount(m)))

#인덱스 슬라이싱(시간초과)
from math import factorial
n,m = map(int,input().split())
count = 0
result = factorial(n) // factorial(n-m) // factorial(m)

for i in str(result)[::-1]:
    if i != '0':
        break
    count += 1
print(count)