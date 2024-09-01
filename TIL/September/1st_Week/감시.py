def bfs(y, x, temp, trial, current_min):
    if current_min >= minimum:
        return
    if type(trial) == int:
        temp[y][x] = 1
        current_min += 1
        while True:
            nx = x + dx[trial]
            ny = y + dy[trial]
            if not (0 <= nx < m and 0 <= ny < n):
                break
            if temp[ny][nx] == 2:
                break
            temp[ny][nx] = 1
            current_min += 1
            y = ny
            x = nx
    else:
        temp[y][x] = 1
        current_min += 1
        o_y = y
        o_x = x
        for idx in trial:
            y = o_y
            x = o_x
            while True:
                if current_min >= minimum:
                    return
                nx = x + dx[idx]
                ny = y + dy[idx]
                if not(0 <= nx < m and 0 <= ny < n):
                    break
                if temp[ny][nx] == 2:
                    break
                temp[ny][nx] = 1
                current_min += 1
                y = ny
                x = nx
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
minimum = int(1e9)
def bfs_five(y, x, temp, current_min):

    temp[y][x] = 1
    current_min += 1
    o_x = x
    o_y = y
    for i in range(4):
        y = o_y
        x = o_x
        while True:
            if current_min >= minimum:
                return
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < m and 0 <= ny < n):
                break
            if temp[ny][nx] == 2:
                break
            temp[ny][nx] = 1
            current_min += 1
            y = ny
            x = nx
req = [[2, 3], [0, 2, 3], [0, 1, 2], 5, 5]
n, m = map(int, input().split())
arr_temp = [[0, 0, 0, 0, 0], [2, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 0, 0]]
start_position = [[1, 1], [1, 4], [2, 3], [3, 0], [3, 3]]
idx = 0
current_min = 0
for t in req:
    if t != 5:
        bfs(start_position[idx][0], start_position[idx][1], arr_temp, t, current_min)
    elif t == 5:
        bfs_five(start_position[idx][0], start_position[idx][1], arr_temp, current_min)
    idx += 1
    # if trial[0] == [2, 3] and trial[1] == [0, 1, 3] and trial[2] == [0, 1, 2]:
    #     print(f't={t} arr_temp = {arr_temp}')

print(arr_temp)
cnt = 0
for i in range(n):
    cnt += arr_temp[i].count(0)
    if cnt >= minimum:
        break
        minimum = min(minimum, cnt)
print(minimum)