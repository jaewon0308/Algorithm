"""
전체 범위로 하면 시간 초과가 나서
소수가 아니려면 절반전에 짝이 있기 때문에
제곱근까지의 범위만 구해주면 된다는 것을
알게 됨
"""
n,m = map(int,input().split())
for i in range(n,m+1):
    if i > 1:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            print(i)