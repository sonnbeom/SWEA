n = int(input())
li = []
for i in range(n):
    tmp = list(map(int, input().split()))
    li.append(tmp)

li.sort(key=sum)


print(li)
res = [0,0,0]

