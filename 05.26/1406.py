import sys
x_l = list(input())
x_r = []
n = int(input())

for i in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L' and x_l:
        x_r.append(x_l.pop())
    elif command[0] == 'D' and x_r:
        x_l.append(x_r.pop())
    elif command[0] == 'B' and x_l:
        x_l.pop()
    elif command[0] == 'P':
        x_l.append(command[1])
print(''.join(x_l+ list(reversed(x_r))))