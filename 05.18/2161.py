x = int(input())
n = [i for i in range(1,x+1)]
result = []

while len(n) != 1:
    result.append(n.pop(0))
    n.append(n.pop(0))

result.append(n.pop())
print(*result)