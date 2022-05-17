x = int(input())
stack = []
for i in range(x):
    stack.append(input().split(' '))

for i in range(len(stack)):
    stack[i].reverse()
    print("Case #%d: %s" %(i+1,' '.join(stack[i])))