'''
1. 해당 위치에서 bfs 때리기
bfs를 돌며
1. 인덱스를 벗어나지 않거나
2. 방문하지 않거나
3. 0인 것이면 전진

2. 위치 추출 함수
주위의 0이 하나라도 있으면 위치 적합
'''

from collections import deque

def bfs(sy, sx, node):
    q = deque()
    q.append((sy, sx))
    visited_node_up[sy][sx] = True
    land[sy][sx] = node
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < N):
                continue
            if visited_node_up[ny][nx]:
                continue
            if land[ny][nx] != 0:
                visited_node_up[ny][nx] = True
                land[ny][nx] = node
                q.append((ny, nx))

def get_possible_node(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < N and 0 <= nx < N):
            continue
        if land[ny][nx] == 0:
            candidate_land.append((y, x))
            return

def get_minimum_bridge(sy, sx):
    global minimum_bridge
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((sy, sx, 0))
    visited[sy][sx] = True

    while q:
        y, x, distance = q.popleft()

        if distance >= minimum_bridge:
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < N):
                continue
            if visited[ny][nx]:
                continue
            if land[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((ny, nx, distance+1))
            elif land[ny][nx] != land[sy][sx]:
                minimum_bridge = min(minimum_bridge, distance)



dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

candidate_land = []
minimum_bridge = int(1e9)

visited_node_up = [[False for _ in range(N)] for _ in range(N)]
node = 1
for y in range(N):
    for x in range(N):
        if land[y][x] == 1:
            get_possible_node(y, x)
            if not visited_node_up[y][x]:
                bfs(y, x, node)
                node += 1

for y, x in candidate_land:
    get_minimum_bridge(y, x)


print(minimum_bridge)
