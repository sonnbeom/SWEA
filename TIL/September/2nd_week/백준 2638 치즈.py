dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def is_cheese_delete(y, x):
    check = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= ny < n and 0 <= nx < m):
            continue
        if arr[ny][nx] == 0:
            check += 1
    if check >= 2:
        remove_list.append((y, x))


def remove_cheese():
    for y, x in remove_list:
        arr[y][x] = 0


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while True:
    check = 0
    remove_list = []
    for y in range(n):
        for x in range(m):
            if arr[y][x] != 0:
                is_cheese_delete(y, x)
                check += 1
    if check == 0:
        break
    remove_cheese()
    cnt += 1

print(cnt)
