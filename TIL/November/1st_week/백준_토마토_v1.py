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
    q = deque()
    for _ in range(len(node_list)):
        h, y, x = node_list.pop(0)
        q.append((h,y,x))
        visited[h][y][x] = True

    while q:
        h, y, x = q.popleft()
        visited[h][y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if visited[h][ny][nx]:
                continue
            if box[h][ny][nx] == 0:
                box[h][ny][nx] = 1
                change_nodes += 1
                node_list.append((h, ny, nx))

        for i in range(2):
            nh = h + dh[i]
            if not(0 <= nh < H):
                continue
            if visited[nh][y][x]:
                continue
            if box[nh][y][x] == 0:
                box[nh][y][x] = 1
                change_nodes += 1
                node_list.append((nh, y, x))

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
node_list = []
for h in range(H):
    for y in range(N):
        for x in range(M):
            if box[h][y][x] == 1:
                node_list.append((h,y,x))

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

while True:
    change_nodes = bfs()
    if change_nodes == 0:
        break
    day += 1

if is_can():
    print(day)
else:
    print(-1)

