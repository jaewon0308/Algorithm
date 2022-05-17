import sys

x_r = list(input())
x_l = []
num = int(sys.stdin.readline())

for i in range(num):
    command = sys.stdin.readline().split()

    if command[0] == 'L' and x_r:
        x_l.append(x_r.pop())
    elif command[0] == 'D' and x_l:
        x_r.append(x_l.pop())
    elif command[0] == 'B' and x_r:
        x_r.pop()
    elif command[0] == 'P':
        x_r.append(command[1])
print(''.join(x_r + list(reversed(x_l))))