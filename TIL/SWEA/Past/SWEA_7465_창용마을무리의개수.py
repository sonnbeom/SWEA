n, m = map(int, input().split())
country = []
for i in range(n+1):
    country.append([])
visited = [False for _ in range(n+1)]
visited[0] = True
for i in range(m):
    a, b = map(int, input().split())
    country[a].append(b)
    country[b].append(a)

isGroup = False
def dfs(node, tmp):
    global isGroup
    if visited[node] == False and len(country[node]) > 0:
        visited[node] = True
        for i in country[node]:
            if visited[i] == False:
                dfs(i, tmp+1)
                isGroup = True

ans = 0
for idx in range(1, n+1):
    dfs(idx, 0)
    if isGroup == True:
        ans += 1
        isGroup = False

solo = visited.count(False)

print(ans + solo)