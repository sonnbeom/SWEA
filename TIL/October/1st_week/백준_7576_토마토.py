def solution (y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < N and 0 <= nx < M):
            continue
        if arr[ny][nx] == 0:
            change_list.append((ny, nx))

def is_success():
    for i in range(N):
        if arr[i].count(0) > 0:
            return False
    return True

def change():
    for y, x in change_list:
        arr[y][x] = 1

M, N = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
go = False

for i in range(N):
    if arr[i].count(0) > 0:
        go = True
        break
if not go:
    print(0)

cnt = 0
while go:
    change_list = []
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1: #and not visited[y][x]
                solution(y, x)
    if len(change_list) == 0:
        success = is_success()
        if not success:
            print(-1)
        else:
            print(cnt)
        break
    cnt += 1
    change()

