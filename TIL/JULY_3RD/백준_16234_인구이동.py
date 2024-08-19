dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]
n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

check_num = 0
cnt = 0

def check_range(y, x):
    if 0 <= y < n and 0 <= x < n and not visited[y][x]:
        return True
    return False

def bfs(y, x, visited):
    global check_num
    p = [] # 좌표
    d = land[y][x] # 거리 합
    p.append((y,x))
    visited[y][x] = True
    q = [(y,x)]
    while q:
        ty, tx = q.pop(0)
        # visited[ty][tx] = True

        for i in range(4):
            now_x = tx + dx[i]
            now_y = ty + dy[i]
            if check_range(now_y, now_x):
                diff = abs(land[now_y][now_x] - land[ty][tx])
                if l <= diff <= r:
                    check_num += 1
                    visited[now_y][now_x] = True
                    p.append((now_y, now_x))
                    d += land[now_y][now_x]
                    q.append((now_y, now_x))
    if len(p) > 1:
        t = d // len(p)
        for ny, nx in p:
            land[ny][nx] = t

while True:
    cnt += 1
    check_num = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                bfs(y, x, visited)

    if check_num == 0:
        break

print(cnt-1)