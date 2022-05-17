x = int(input())
answer = []
for i in range(x):
    a = input()
    if a == '0':
        if answer:
            answer.pop()
    else:
        answer.append(a)

answer = list(map(int,answer))
print(sum(answer))