import itertools
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split()) # n 세로 :y m 가로: x

arr = [list(map(int, input().split())) for _ in range(n)]

z = []
virus = []
maximum = 0
def bfs(tmp):
    global maximum

    visited = [[False for _ in range(m)] for _ in range(n)]
    q = []
    for y, x in virus:
        q.append((y,x))
        visited[y][x] = True
    while q:
        tmp_y, tmp_x = q.pop(0)
        for i in range(4):
            ny = tmp_y + dy[i]
            nx = tmp_x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and tmp[ny][nx] == 0:
                    visited[ny][nx] = True
                    tmp[ny][nx] = 2
                    q.append((ny, nx))
    res = 0
    for i in range(n):
        res += tmp[i].count(0)

    maximum = max(res, maximum)


for y in range(n):
    for x in range(m):
        if arr[y][x] == 2:
            virus.append((y, x))
        elif arr[y][x] == 0:
            z.append((y, x))


candidate = list(itertools.combinations(z, 3))
for li in candidate:
    c = copy.deepcopy(arr)
    for y, x in li:
        c[y][x] = 1
    bfs(c)
print(maximum)