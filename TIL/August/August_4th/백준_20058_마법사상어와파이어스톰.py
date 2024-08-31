from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, Q = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(2**N)]
q_list = list(map(int, input().split()))
# range(start, end, step)는
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
visited_near_ice = [[0 for _ in range(2**N)] for _ in range(2**N)]
maximum_ice_box = 0
def rotate(q, y, x):
    tmp_list = []
    for tx in range(x, 2**q+x):
        tmp = []
        for ty in range(y+2**q-1, y-1, -1):
            tmp.append(ice[ty][tx])
        tmp_list.append(tmp)
    tmp_y = tmp_x = 0
    for ty in range(y, y+2**q):
        for tx in range(x, x+2**q):
            ice[ty][tx] = tmp_list[tmp_y][tmp_x]
            visited[ty][tx] = 1
            tmp_x += 1
        tmp_x = 0
        tmp_y += 1

def ice_minus():
    ice_minus_list = []
    for y in range(2**N):
        for x in range(2**N):
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if not(0 <= ny < 2 ** N and 0 <= nx < 2 ** N and ice[ny][nx] != 0):
                    cnt += 1
            if cnt >= 2:
                ice_minus_list.append((y, x))
    for y, x in ice_minus_list:
        if ice[y][x] != 0:
            ice[y][x] -= 1
# 얼음 숫자 감소와 인접해있는 것들에 대한 탐색을 나누자!
def bfs(req_y, req_x):
    global maximum_ice_box

    q = deque()
    q.append((req_y, req_x))
    visited_near_ice[req_y][req_x] = 1 # 1이 방문
    ice_cnt = 1

    while q:
        y, x = q.popleft()
        visited_near_ice[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 2**N and 0 <= nx < 2**N and ice[ny][nx] != 0:
                if visited_near_ice[ny][nx] != 1:
                    q.append((ny, nx))
                    ice_cnt += 1
                    visited_near_ice[ny][nx] = 1
    maximum_ice_box = max(maximum_ice_box, ice_cnt)

for i in range(Q):
    q = q_list[i]
    visited = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    if q != 0:
        for y in range(2 ** N):
            for x in range(2 ** N):
                if visited[y][x] != 1:
                    rotate(q, y, x)
    ice_minus()
    if i == Q-1:
        for y in range(2 ** N):
            for x in range(2 ** N):
                if visited_near_ice[y][x] != 1 and ice[y][x] != 0:
                    bfs(y, x)

sum_ice = 0
for i in range(2**N):
    sum_ice += sum(ice[i])


print(sum_ice)
print(maximum_ice_box)
