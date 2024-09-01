dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

trial_list =[]

def dfs(idx ,depth, temp_arr):
    if depth == length:
        trial_list.append(temp_arr.copy())
        return

    arr_len = len(dfs_list[idx])
    for i in range(arr_len):
        node = dfs_list[idx][i]
        if not visited[idx][i]:
            temp_arr.append(node)
            visited[idx][i] = True
            dfs(idx+1, depth+1, temp_arr)
            visited[idx][i] = False
            temp_arr.pop()
def spy(y, x, temp, trial):
    if type(trial) == int:
        temp[y][x] = 1
        while True:
            nx = x + dx[trial]
            ny = y + dy[trial]
            if not (0 <= nx < m and 0 <= ny < n):
                break
            if temp[ny][nx] == 2:
                break
            temp[ny][nx] = 1
            y = ny
            x = nx
    else:
        temp[y][x] = 1
        o_y = y
        o_x = x
        for idx in trial:
            y = o_y
            x = o_x
            while True:
                nx = x + dx[idx]
                ny = y + dy[idx]
                if not(0 <= nx < m and 0 <= ny < n):
                    break
                if temp[ny][nx] == 2:
                    break
                temp[ny][nx] = 1
                y = ny
                x = nx


def spy_5(y, x, temp):

    temp[y][x] = 1
    o_x = x
    o_y = y
    for i in range(4):
        y = o_y
        x = o_x
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < m and 0 <= ny < n):
                break
            if temp[ny][nx] == 2:
                break
            temp[ny][nx] = 1
            y = ny
            x = nx



def append_visited(arr_len):
    v = [False for _ in range(arr_len)]
    visited.append(v)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

one = [0, 1, 2, 3]
two = [[0, 1], [2, 3]]
three = [[1, 2], [0, 2], [1, 3], [0, 3]]
four = [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]]
five = [5]

start_position = []
wall = []
dfs_list = []
visited = []
visited_bfs = [[False for _ in range(m)] for _ in range(n)]
for y in range(n):
    for x in range(m):
        if arr[y][x] != 0 and arr[y][x] != 6:
            start_position.append([y, x])
            if arr[y][x] == 1:
                dfs_list.append(one)
                append_visited(len(one))
            elif arr[y][x] == 2:
                dfs_list.append(two)
                append_visited(len(two))
            elif arr[y][x] == 3:
                dfs_list.append(three)
                append_visited(len(three))
            elif arr[y][x] == 4:
                dfs_list.append(four)
                append_visited(len(four))
            else:
                dfs_list.append(five)
                append_visited(len(five))
        elif arr[y][x] == 6:
            wall.append([y, x])
length = len(start_position)

dfs(0, 0, [])


minimum = int(1e9)
wall_cnt = len(wall)
square_cnt = n * m
max_cnt = square_cnt - wall_cnt

for trial in trial_list:
    arr_temp = [[0 for _ in range(m)] for _ in range(n)]
    for y, x in wall:
        arr_temp[y][x] = 2
    idx = 0
    current = max_cnt
    for t in trial:
        if t != 5:
            spy(start_position[idx][0], start_position[idx][1], arr_temp, t)
        elif t == 5:
            spy_5(start_position[idx][0], start_position[idx][1], arr_temp)
        idx += 1
    cnt = 0
    for i in range(n):
        cnt += arr_temp[i].count(0)
        if cnt >= minimum:
            break
    minimum = min(minimum, cnt)
print(minimum)
