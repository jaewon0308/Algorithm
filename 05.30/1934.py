n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    xx,yy = x,y
    while y:
        x,y = y,x%y
    print((xx*yy)//x)