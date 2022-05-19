import sys

x = int(sys.stdin.readline())
for i in range(1,x+1):
    n = int(sys.stdin.readline())
    number = sorted(map(int,sys.stdin.readline().split()),reverse=True)
    result = []

    while number:
        price = number.pop()
        if price * 100//75 in number:
            result.append(str(price))
            number.remove(price * 100//75)
    print('Case #%d: %s' %(i,' '.join(result)))