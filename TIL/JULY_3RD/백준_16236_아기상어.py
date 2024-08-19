dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

def get_spot(size):
    pos = []
    for y in range(n):
        for x in range(n):
            if sea[y][x] < size:
                pos.append((y, x))
def bfs(y, x, target, size):
    q = [(y, x, 0)]
    min_dis = 0
    res_y = 0
    res_x = 0
    can_go = False
    visited = [[False for _ in range(n)] for _ in range(n)
    visited[y][x] = True
    while q:
        tmp_y, tmp_x , d = q.pop(0)
        for i in range(4):
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if sea[ny][nx] <= size and visited[ny][nx]:
                    if ny == target[0] and nx == target[1]:
                        res_y = ny
                        res_x = nx
                        min_dis = d + 1
                        can_go = True
                        q.clear()
                        break
                    q.append((ny, nx, d + 1))
    return min_dis, can_go, res_y, res_x

size = 2
cnt = 0
while True:
    pos = []
    shark = (-1, -1)
    for y in range(n):
        for x in range(n):
            if sea[y][x] < size:
                pos.append((y, x))
            if sea[y][x] == 9:
                shark[0] = y
                shark[1] = x
    if len(pos) == 0:
        break
    min_dis = 10000
    tmp_spot = []
    for ty, tx in pos:
        res = bfs(shark[0], shark[1], (ty, tx), size)
        if res[1] == True:
            tmp_spot.append(res)
    tmp_spot.sort()
    goal = tmp_spot[0]
    cnt += goal[0]
