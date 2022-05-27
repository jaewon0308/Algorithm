"""
문제의 주어진 조건을 먼저 파악하고 수식화, 규칙 찾기의 중요성을
알려주는 문제다.
문제 이해도를 높이자
"""
n = list(input())
stack = []
result = 0

for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    else:
        if n[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)