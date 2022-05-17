import sys
num = int(input())
for i in range(num):
    x = sys.stdin.readline().strip()
    x_l = []
    x_r = []
    for j in x:
        if j == '<':
            if x_l:
                x_r.append(x_l.pop())
        elif j == '>':
            if x_r:
                x_l.append(x_r.pop())
        elif j == '-':
            if x_l:
                x_l.pop()
        else:
            x_l.append(j)
    x_l.extend(reversed(x_r))
    print(''.join(x_l))