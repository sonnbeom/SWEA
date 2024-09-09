'''
각 방향을 적고
순회를 한다
ex 1이 나오면 순회를 하고
idx가 벗어나지 않고 방문하지 않은 곳이라면

two를 for문 돈다
ny, nx의 좌표 값을 가져온다
예를 들어 4라고 가정해보자
다시 4를 for문을 돈다
만약 음수를 붙인 값이 존재한다면 해당 노드는 방문할 수 있는 노드다
방문 처리하고 cnt +=1

'''



dx = [-1, 1, 0, 0] # 좌우 상하
dy = [0, 0, 1, -1] # 좌우 상하

one = [(0, -1), (0, 1), (1, 0), (-1, 0)]
two = [(1,0), (-1,0)]
thr = [(0,-1), (0,1)]
four = [(-1,0), (0,1)]
five = [(1,0), (0,1)]
six = [(0, -1), (1,0)]
sev = [(0,-1), (-1,0)]
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
        return 1
    return 0

cnt = 0

def bfs(ty,tx):
    global cnt

    q = deque()
    q.append((ty, tx, 1))
    visited[ty][tx] = True
    while q:
        y, x, time = q.popleft()
        if time > L:
            continue
        now = tunnel[y][x]
        direction = transfer(now)
        for i in range(4):
            if not (dy[i], dx[i]) in direction:
                continue
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if tunnel[ny][nx] == 0 or visited[ny][nx]:
                continue
            cnt += go(dy[i], dx[i], tunnel[ny][nx])
            visited[ny][nx] = True
            q.append((ny, nx, time+1))

from collections import deque
N, M, R, C, L = map(int,input().split())

tunnel = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
bfs(R, C)
print(cnt)
print(visited)
