'''
1. 한칸씩 내리는 법

맨 아래 y축 값에서 0이라면 가장 위에있는 값을 불러오고 그 값은 0으로 처리 이러한 과정을 반복한다.
정확히는
맨 아래 y축에서 0이 나오고 그 다음 숫자가 나오는 것을 리스트에 담고 방문한 곳은 0으로 채운다
그리고 그걸 리스트에 담고 0이 시작한 곳부터 넣은 뒤 뺀 뒤에 pop

2. 벽돌 크러쉬
벽돌 크러쉬를 한다. q에 넣는 형식
벽돌을 0으로 만든 뒤 그 값이 1과 0이 아니라면 그 위치 즉 ny, nx, 해당 값을 q에 넣는다
좌, 우, 상, 하를 해당 값만큼 전진하며 크러쉬한다.
1 과 0이 아니라면 q가 무한반복된다.


'''
from collections import deque
from copy import deepcopy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def get_next_y(x, arr):
    for i in range(h):
        if arr[i][x] != 0:
            return i
    return -1
def down(x, arr):
    tmp_list = []
    go = False
    idx = 0
    for i in range(h-1, -1, -1):
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
            for s in range(size-1): # 더하고 tmp_x를 nx tmp_y를 ny로 바꿔야 한다
                ny = tmp_y + dy[i]
                nx = tmp_x + dx[i]

                if not(0 <= ny < h and 0 <= nx < w):
                    continue
                if arr[ny][nx] == 1:
                    temp_cnt -= 1
                    arr[ny][nx] = 0
                elif arr[ny][nx] != 1 and arr[ny][nx] != 0:
                    if (ny,nx) not in visited:
                        q.append((ny, nx, arr[ny][nx]))
                        visited.append((ny,nx))
                tmp_y = ny
                tmp_x = nx

def dfs(depth, temp):
    global trial_list
    if depth == n:
        trial_list.append(temp.copy())
        return
    for i in range(w):
        temp.append(i)
        dfs(depth+1, temp)
        temp.pop()

n, w, h = map(int,input().split())
original_arr = [list(map(int,input().split())) for _ in range(h)]

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

print(cnt)
# arr = deepcopy(original_arr)
# temp_cnt = brick
# visited = [[False for _ in range(w)] for _ in range(h)]
# for t in ex:
#     ty = get_next_y(t, arr)
#     if ty == -1:
#         continue
#     bfs(ty, t, arr)
#     for i in range(w):
#         down(i, arr)
# cnt = min(temp_cnt, cnt)
# print(f'temp_cnt = {temp_cnt} cnt = {cnt}')

