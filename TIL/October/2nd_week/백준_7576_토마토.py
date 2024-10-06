from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs():
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for sy, sx in start_list:
        q.append((sy, sx))
        visited[sy][sx] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < M):
                continue

            if arr[ny][nx] == -1:
                continue

            if visited[ny][nx]:
                continue

            arr[ny][nx] = arr[y][x] + 1
            q.append((ny, nx))
            visited[ny][nx] = True


M, N = map(int, input().split()) # m은 가로 n은 세로
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

start_list = []
not_tomato = 0

for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            start_list.append((y, x))
        else:
            not_tomato += 1
check = False
is_success = True
if not_tomato == 0:
    ans = 0
elif len(start_list) == 0:
    ans = -1
else:
    check = True
    bfs()
    for i in range(N):
        for j in range(M):
            ans = max(ans, arr[i][j])
            if arr[i][j] == 0:
                is_success = False
                ans = -1
                break
if not check:
    print(ans)
else:
    if is_success:
        print(ans-1)
    else:
        print(-1)