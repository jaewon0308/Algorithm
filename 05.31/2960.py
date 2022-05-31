"""
내가 알고 있는 에라토스테네스의 체는
소수 자기 자신을 제외한 수를 제거해야하는데
이 문제는 자기 자신도 제거하는 순서에
포함했기 때문에 이해하는데 내가 잘못알고
있나?라고 헷갈리게 됨
원래는 자기 자신 제외하고 제거임
특이한 문제다
"""
n,k = map(int,input().split())
count = 0
arr = [True for i in range(n+1)]
for i in range(2,n+1):
    for j in range(i,n+1,i):
        if arr[j]:
            arr[j] = False
            count += 1
            if count == k:
                print(j)