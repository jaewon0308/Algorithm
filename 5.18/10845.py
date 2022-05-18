import sys
x = int(sys.stdin.readline())
stack = []

for i in range(x):
    n = sys.stdin.readline().split()

    if n[0] == 'push':
        stack.insert(0,n[1])
    elif n[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif n[0] == 'size':
        print(len(stack))
    elif n[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif n[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])