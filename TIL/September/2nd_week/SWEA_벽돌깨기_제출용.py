from collections import deque
from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def get_next_y(x, arr):
    for i in range(h):
        if arr[i][x] != 0:
            return i
    return -1


def down(x, arr):
    tmp_list = []
    go = False
    idx = 0
    for i in range(h - 1, -1, -1):
        if arr[i][x] == 0 and not go:
            go = True
            idx = i
        elif arr[i][x] != 0 and go:
            tmp_list.append(arr[i][x])
            arr[i][x] = 0

    if tmp_list:
        for tmp in tmp_list:
            arr[idx][x] = tmp
            idx -= 1


def bfs(ty, tx, arr):
    global temp_cnt

    q = deque()
    q.append((ty, tx, arr[ty][tx]))
    arr[ty][tx] = 0
    visited = []
    while q:
        y, x, size = q.popleft()
        temp_cnt -= 1
        arr[y][x] = 0

        for i in range(4):
            tmp_y = y
            tmp_x = x
            for s in range(size - 1):  # 더하고 tmp_x를 nx tmp_y를 ny로 바꿔야 한다
                ny = tmp_y + dy[i]
                nx = tmp_x + dx[i]

                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if arr[ny][nx] == 1:
                    temp_cnt -= 1
                    arr[ny][nx] = 0
                elif arr[ny][nx] != 1 and arr[ny][nx] != 0:
                    if (ny, nx) not in visited:
                        q.append((ny, nx, arr[ny][nx]))
                        visited.append((ny, nx))
                tmp_y = ny
                tmp_x = nx


def dfs(depth, temp):
    global trial_list
    if depth == n:
        trial_list.append(temp.copy())
        return
    for i in range(w):
        temp.append(i)
        dfs(depth + 1, temp)
        temp.pop()


t = int(input())
for tc in range(1, t+1):
    n, w, h = map(int, input().split())
    original_arr = [list(map(int, input().split())) for _ in range(h)]

    brick = 0

    for y in range(h):
        for x in range(w):
            if original_arr[y][x] != 0:
                brick += 1
    cnt = brick

    trial_list = []
    dfs(0, [])
    # 1 1 3
    for trial in trial_list:
        if cnt == 0:
            break
        temp_cnt = brick
        arr = deepcopy(original_arr)

        for t in trial:
            ty = get_next_y(t, arr)
            if ty == -1:
                continue
            bfs(ty, t, arr)
            if temp_cnt == 0:
                cnt = 0
                break
            for i in range(w):
                down(i, arr)
        cnt = min(temp_cnt, cnt)

    print(f'#{tc} {cnt}')