from collections import deque

def bfs():
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < n and 0 <= nx < m):
                continue
            if visited[ny][nx]:
                continue
            if arr[ny][nx] != 0:
                arr[ny][nx] += 1
            else:
                visited[ny][nx] = True
                q.append((ny, nx))

def melt_cheese():
    success = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] >= 3:
                arr[y][x] = 0
                success += 1
            elif arr[y][x] == 2:
                arr[y][x] = 1
    return success

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

while True:
    bfs()
    time = melt_cheese()
    if time != 0:
        cnt += 1
    elif time == 0:
        break
print(cnt)