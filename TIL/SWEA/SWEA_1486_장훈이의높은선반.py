n, top = map(int, input().split())

height = list(map(int, input().split()))
maxHeight = sum(height)
visited = [False for _ in range(maxHeight+1)]

temp = [0]

for h in height:
    for i in range(len(temp)):
        if visited[h + temp[i]] == False:
            visited[h + temp[i]] = True
            temp.append(h+temp[i])
ans = 0
for i in range(top, maxHeight+1):
    if visited[i] == True:
        ans = i
        break
print(ans- top)