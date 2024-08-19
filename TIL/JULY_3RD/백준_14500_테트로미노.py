dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split()) # n이 세로 = y
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
maximum = 0

def dfs(y, x, tmp, depth):
    global maximum
    if depth == 4:
        maximum = max(tmp, maximum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, tmp + paper[ny][nx], depth + 1)
            visited[ny][nx] = False

def o(y, x):
    global maximum
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            arr.append(paper[ny][nx])
    l = len(arr)

    if l == 4:
        arr.sort()
        arr.pop(0)
        maximum = max(maximum, sum(arr) + paper[y][x])

    elif l == 3:
        maximum = max(maximum, sum(arr) + paper[y][x])

    return

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(y, x, paper[y][x], 1)
        o(y, x)
        visited[y][x] = False

print(maximum)