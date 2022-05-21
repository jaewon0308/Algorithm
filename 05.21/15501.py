"""
deque 사용해서 해보려했다가 복잡해져서 리스트로 구성해 쉽게 해보았다
deque로 계속 해보려는 시도 때문에 시간이 많이 걸렸지만
유도리있게 새로운 방법을 찾아보았음
안되면 새로운 방법 찾아내는 능력을 기르자
"""
x = int(input())
queue = list(map(int,input().split()))
compare = list(map(int,input().split()))

right = compare.index(queue[0])
right_com = compare[right:] + compare[:right]

compare = compare[::-1]
right = compare.index(queue[0])
left_com = compare[right:] + compare[:right]

if queue == right_com or queue == left_com:
    print('good puzzle')
else:
    print('bad puzzle')