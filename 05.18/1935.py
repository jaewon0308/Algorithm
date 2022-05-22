x = int(input())
word = input()
num = [0] * x
stack = []
for i in range(x):
    num[i] = int(input())

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i)-ord('A')])
    else:
        temp1 = stack.pop()
        temp2 = stack.pop()

        if i == '+':
            stack.append(temp2 + temp1)
        elif i == '-':
            stack.append(temp2 - temp1)
        elif i == '*':
            stack.append(temp2 * temp1)
        elif i == '/':
            stack.append(temp2 / temp1)
print('%.2f'%stack[0])