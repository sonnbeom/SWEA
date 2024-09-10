def transfer(req):
    if req <= 3:
        return transfer_under_four(req)
    else:
        return transfer_over_four(req)


def transfer_under_four(req):
    if req == 1:
        return one
    elif req == 2:
        return two
    elif req == 3:
        return thr


def transfer_over_four(req):
    if req == 4:
        return four
    elif req == 5:
        return five
    elif req == 6:
        return six
    else:
        return sev


def go(dir_y, dir_x, next):
    next = transfer(next)
    next_y = dir_y * - 1
    next_x = dir_x * - 1
    if (next_y, next_x) in next:
        return True
    return False

def bfs(ty, tx):
    global cnt

    q = deque()
    q.append((ty, tx, 1))
    visited[ty][tx] = True
    while q:
        y, x, time = q.popleft()
        cnt += 1
        now = tunnel[y][x]
        direction = transfer(now)
        for i in range(4):
            if not (dy[i], dx[i]) in direction:
                continue
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if tunnel[ny][nx] == 0 or visited[ny][nx]:
                continue
            res = go(dy[i], dx[i], tunnel[ny][nx])
            if res:
                visited[ny][nx] = True
                if time + 1 <= L:
                    q.append((ny, nx, time + 1))

from collections import deque
dx = [-1, 1, 0, 0]  # 좌우 상하
dy = [0, 0, 1, -1]  # 좌우 상하

one = [(0, -1), (0, 1), (1, 0), (-1, 0)]
two = [(1, 0), (-1, 0)]
thr = [(0, -1), (0, 1)]
four = [(-1, 0), (0, 1)]
five = [(1, 0), (0, 1)]
six = [(0, -1), (1, 0)]
sev = [(0, -1), (-1, 0)]
t = int(input())
for tc in range(1, t+1):
    cnt = 0
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    bfs(R, C)
    print(f'#{tc} {cnt}')

