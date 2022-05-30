"""
math함수를 알고 있지만 안쓰고 구현해보았다
1. for문으로 만들기
2. 유클리드 호제법으로 만들기
3. math함수 사용하기
"""
x,y = map(int,input().split())

#for문으로 만들기
def gcd(x,y):
    for i in range(min(x,y),0,-1):
        if x%i == 0 and y%i == 0:
            print(i)
            break

def lcm(x,y):
    for i in range(min(x,y),0,-1):
        if x%i == 0 and y%i == 0:
            print((x//i)*(y//i)*i)
            break
gcd(x,y)
lcm(x,y)

#유클리드 호제법으로 만들기
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x


def lcm(x,y):
    result = (x*y) //gcd(x,y)
    return result

print(gcd(x,y))
print(lcm(x,y))

#math함수 사용하기
import math

print(math.gcd(x,y))
print(math.lcm(x,y))
