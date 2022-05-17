***
소요시간 10분
***
x = int(input())
y = list(map(int,input().split()))
z = []
for i in range(1,x+1)
    z.insert(y[i-1],i)
z.reverse()

print(z)