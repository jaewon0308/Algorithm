"""
처음에 word, answer를 List로 만들어서 옮길 때 불편해서 방법을 변경함
"""
x = input()
word = ""
answer = ""
count = False

for i in x:
    if count == False:
        if i == '<':
            count = True
            word += i
        elif i == " ":
            word += i
            answer += word
            word = ""
        else:
            word = i + word
    else:
        word += i
        if i == '>':
            answer += word
            word = ""
            count = False
print(answer + word)