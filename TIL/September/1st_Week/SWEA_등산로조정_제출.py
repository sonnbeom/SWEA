

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def func(length, ty, tx, chance, height):
    global max_len
    max_len = max(max_len, length)
    for i in range(4):
        ny = ty + dy[i]
        nx = tx + dx[i]
        if not (0 <= ny < n and 0 <= nx < n):
            continue
        if visited[ny][nx]:
            continue
        if mountain[ny][nx] < height:
            visited[ny][nx] = True
            func(length + 1, ny, nx, chance, mountain[ny][nx])
            visited[ny][nx] = False
        elif chance != 0 and mountain[ny][nx] - k < height:
            visited[ny][nx] = True
            # func(length + 1, ny, nx, 0, mountain[ny][nx] - k)
            func(length + 1, ny, nx, 0, height-1)
            visited[ny][nx] = False


t = int(input())
for tc in range(1, t+1):
    max_len = 0
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    start = []
    max_height = 0
    for y in range(n):
        for x in range(n):
            max_height = max(max_height, mountain[y][x])
    for y in range(n):
        for x in range(n):
            if mountain[y][x] == max_height:
                start.append((y, x))
    for y, x in start:
        visited[y][x] = True
        func(1, y, x, 1, mountain[y][x])
    print(f'#{tc} {max_len}')

