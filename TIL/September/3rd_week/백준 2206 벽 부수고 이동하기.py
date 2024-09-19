from collections import deque
from copy import deepcopy
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def move():
    global ans
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append((0, 0, 1, 1)) # y, x, 거리, 기회
    visited[0][0] = True

    while q:
        y, x, distance, chance = q.popleft()
        # print(f'y= {y} x ={x} chance = {chance}')
        if y == N-1 and x == M-1:
            ans = min(ans, distance)
            return
        elif distance >= ans:
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if visited[ny][nx]:
                continue
            if arr[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((ny, nx, distance+1, chance))
            else:
                if chance == 1 and not visited_broken[ny][nx]:
                    dfs(ny, nx, distance+1)
                    visited_broken[ny][nx] = True
                    visited[ny][nx] = True

def dfs(y, x, d):
    global ans
    if d >= ans:
        return
    elif y == N-1 and x == M-1:
        ans = min(ans, d)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= nx < M and 0 <= ny < N):
            continue
        if visited_broken[ny][nx]:
            continue
        if arr[ny][nx] == 0:
            visited_broken[ny][nx] = True
            dfs(ny, nx, d+1)






ans = int(1e9)
INF = ans
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited_broken = [[False for _ in range(M)] for _ in range(N)]
move()
if ans == INF:
    print(-1)
else:
    print(ans)
