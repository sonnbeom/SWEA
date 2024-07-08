t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(1, t+1):
    n = int(input())
    snail = [[0] * n for j in range(n)]

    x = 0
    y = 0
    direc = 0

    for num in range(1, n*n + 1):
        snail[y][x] = num
        x += dx[direc]
        y += dy[direc]

        if x < 0 or y < 0 or x >= n or y >= n or snail[y][x] != 0:
            x -= dx[direc]
            y -= dy[direc]

            direc = (direc+1) % 4
            x += dx[direc]
            y += dy[direc]

    print("#", i, sep='')
    for answer in snail:
        print(*answer)



