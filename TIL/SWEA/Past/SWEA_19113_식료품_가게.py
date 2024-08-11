
TC = int(input())

for i in range(1, TC+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = []
    for price in arr:
        original = price*4/3
        if original in arr:
            answer.append(price)
            arr.remove(original)
    answer.sort
    print("#",i,sep='', end=" ")
    print(*answer)

