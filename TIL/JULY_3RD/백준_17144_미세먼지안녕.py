upper_dx = [1, 0, -1, 0]
upper_dy = [0, -1, 0, 1]
lower_dx = [1, 0, -1, 0]
lower_dy = [0, 1, 0, -1]

def upper_clear_func():
    ty, tx = air_clear[0]
    y, x = air_clear[0]
    prev = 0
    for dir in range(4):
        while True:
            ny = y + upper_dy[dir]
            nx = x + upper_dx[dir]
            if ny == ty and nx == tx:

                break
            if 0 <= ny < n and 0 <= nx < m:
                tmp = room[ny][nx]
                room[ny][nx] = prev
                prev = tmp
                y, x = ny, nx
            else:
                break
def lower_clear_func():
    ty, tx = air_clear[1]
    y, x = air_clear[1]
    prev = 0
    for dir in range(4):
        while True:
            ny = y + lower_dy[dir]
            nx = x + lower_dx[dir]
            if ny == ty and nx == tx:
               break
            if 0 <= ny < n and 0 <= nx < m:
                tmp = room[ny][nx]
                room[ny][nx] = prev
                prev = tmp
                y, x = ny, nx
            else:
                break

def diffuse():
    tmp = []
    for y, x in over_five:
        dust = room[y][x]
        diffusion = dust // 5
        diffusion_count = 0
        for i in range(4):
            ny = y + upper_dy[i]
            nx = x + upper_dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if room[ny][nx] != -1:
                    tmp.append((ny, nx, diffusion))
                    diffusion_count += 1
        if diffusion_count != 0:
            tmp.append((y, x, -(diffusion * diffusion_count)))
    for i in range(len(tmp)):
        y, x, d = tmp[i]
        room[y][x] += d



n, m, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

air_clear = []

for y in range(n):
    for x in range(m):
        if room[y][x] == -1:
            air_clear.append((y, x))

for i in range(t):
    over_five = []
    for y in range(n):
        for x in range(m):
            if room[y][x] >= 5:
                over_five.append((y, x))
    diffuse()
    upper_clear_func()
    lower_clear_func()

ans = 2
for k in range(n):
    ans += sum(room[k])

print(ans)
