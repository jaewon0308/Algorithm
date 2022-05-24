def hanoi(n,start,end):
    hanoisub(n,start,end,2)

def hanoisub(x,start,end,other):
    if x == 1:
        move.append([start,end])
    else:
        hanoisub(x-1,start,other,end)
        move.append([start,end])
        hanoisub(x-1,other,end,start)
move = []
hanoi(int(input()),1,3)

print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))