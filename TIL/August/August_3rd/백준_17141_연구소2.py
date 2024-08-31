from collections import deque
import itertools
from copy import deepcopy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def can(visited, n):
    for i in range(n):
        if 0 in visited[i]:
            return False
    return True

def bfs(position, n, arr, wall):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    distance = 0
    q = deque([])

    for y, x in position:
        arr[y][x] = 0
        q.append((y, x, 0))
        visited[y][x] = 1
        if arr[y][x] == 2 and (y, x) not in position:
            arr[y][x] = 0
    for y, x in wall:
        visited[y][x] = 1
    while q:
        y, x, d = q.popleft()
        if d >= minimum:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] != 1 and arr[ny][nx] != 1:
                visited[ny][nx] = 1
                q.append((ny, nx, d+1))
                distance = max(distance, d+1)

    is_can = can(visited, n)
    if is_can:
        return distance
    else:
        return -1

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

candidate = []
wall = []
for y in range(n):
    for x in range(n):
        if lab[y][x] == 2:
            candidate.append((y, x))
        elif lab[y][x] == 1:
            wall.append((y, x))
minimum = int(1e9)
permutation = itertools.permutations(candidate, m)
permutation = set(tuple(sorted(p)) for p in permutation)
print(permutation)
for p in permutation:
    lab_copy = deepcopy(lab)
    res = bfs(p, n, lab_copy, wall)

    if res != -1:
        minimum = min(minimum, res)
if minimum == int(1e9):
    print(-1)
else:
    print(minimum)

