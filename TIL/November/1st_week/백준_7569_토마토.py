from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
dh = [1, -1]

def is_can():
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if box[h][y][x] == 0:
                    return False
    return True
def bfs():
    change_nodes = 0
    start_list = []
    for hei in range(H):
        for y in range(N):
            for x in range(M):
                if box[hei][y][x] == 1:
                     start_list.append((hei, y, x))
    q = deque()
    for h, y, x in start_list:
        q.append((h,y,x))
    while q:
        h, y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if box[h][ny][nx] == 0:
                box[h][ny][nx] = 1
                change_nodes += 1

        for i in range(2):
            nh = h + dh[i]
            if not(0 <= nh < H):
                continue
            if box[nh][y][x] == 0:
                box[nh][y][x] = 1
                change_nodes += 1

    return change_nodes

# 가로: m 세로:n 높이: h
M, N, H = map(int, input().split())
box = []
for i in range(H):
    temp = []
    for i in range(N):
        input_list = list(map(int, input().split()))
        temp.append(input_list)
    box.append(temp)
day = 0

while True:
    change_nodes = bfs()
    if change_nodes == 0:
        break
    day += 1

if is_can():
    print(day)
else:
    print(-1)

