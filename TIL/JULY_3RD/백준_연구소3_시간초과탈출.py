from collections import deque
import itertools
from copy import deepcopy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(virus, arr, wall, zero_count):
    global minimum, go
    can_go = False
    distance = 0

    q = deque([])

    visited = [[0 for _ in range(n)] for _ in range(n)]

    for y, x in virus:
        q.append((y, x, 0))
        visited[y][x] = 1

    for y, x in wall:
        visited[y][x] = 1
    while q:
        ty, tx, d = q.popleft()
        if d >= minimum:
            can_go = False
            break
        if zero_count == 0:
            can_go = True
            break
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and visited[ny][nx] != 1:
                if arr[ny][nx] == 0:
                    zero_count -= 1
                visited[ny][nx] = 1
                arr[ny][nx] = 2
                q.append((ny, nx, d + 1))
                distance = max(distance, d+1)

    if can_go:
        minimum = min(minimum, distance)

minimum = int(1e9)

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
candidate = []
wall = []
go = True
virus_cnt = 0
wall_cnt = 0
for y in range(n):
    for x in range(n):
        if lab[y][x] == 2:
            candidate.append((y,x))
            virus_cnt += 1
        elif lab[y][x] == 1:
            wall.append((y,x))
            wall_cnt += 1

permutation = itertools.combinations(candidate, m)

zero_cnt = n * n - virus_cnt - wall_cnt
for virus in permutation:
    lab_copy = deepcopy(lab)
    bfs(virus, lab_copy, wall, zero_cnt)

if minimum != int(1e9):
    print(minimum)
else:
    print(-1)