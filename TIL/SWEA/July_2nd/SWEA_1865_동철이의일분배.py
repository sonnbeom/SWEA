n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
total = []
m = 0
def dfs(depth, li):
    global m
    if depth == n:
        if sum(li) > m:
            total.append(li.copy())
            m = sum(li)
        return
    for i in range(n):
        if visited[i] == False:
            li.append(arr[depth][i])
            visited[i] = True
            dfs(depth+1, li)
            li.pop()
            visited[i] = False

dfs(0,[])
print(*total)
tmp = total[-1]
ans = 1
for i in tmp:
    ans *= i/100
r = ans * 100
result = f"{r:6f}"
print(result)
