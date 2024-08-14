n, m = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
for y in range(n):
    for x in range(n):
        if cities[y][x] == 2:
            chicken.append((y,x))
        elif cities[y][x] == 1:
            home.append((y,x))

tryList = []
visited = [False for _ in range(len(chicken))]
def dfs(start, depth, arr):
    if depth == m:
        tryList.append(arr.copy())
        return
    for i in range(start, len(chicken)):
        arr.append(chicken[i])
        dfs(i+1, depth + 1, arr)
        arr.pop()

ans = 100000000
dfs(0,0, [])


distance = 1000000000
for li in tryList:
    t = 0
    for hy, hx in home:
        d = 10000000000
        for ty, tx in li:
            d = min(d, abs(hy-ty) + abs(hx - tx))
        t += d
    distance = min(t, distance)
print(distance)