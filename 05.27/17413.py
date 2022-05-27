n = input()
word = ""
result = ""
temp = False

for i in n:
    if temp == False:
        if i == '<':
            temp = True
            word += i
        elif i == ' ':
            word += i
            result += word
            word = ""
        else:
            word = i + word
    else:
        word += i
        if i == '>':
            result += word
            word = ''
            temp = False
print(result + word)