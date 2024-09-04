n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]
maximum = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
def dfs(y, x, depth, tmp):
    global maximum

    if depth == 4:
        maximum = max(maximum, tmp)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth+1, tmp+paper[ny][nx])
            visited[ny][nx] = False
def get_wo(y, x):
    global maximum
    tmp_arr = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            tmp_arr.append(paper[ny][nx])
    length = len(tmp_arr)

    if length == 3:
        maximum = max(maximum, sum(tmp_arr) + paper[y][x])

    elif length == 4:
        tmp_arr.sort()
        tmp_arr.pop(0)
        maximum = max(maximum, sum(tmp_arr)+paper[y][x])
    return

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(y, x, 1, paper[y][x])
        get_wo(y, x)
        visited[y][x] = False
print(maximum)