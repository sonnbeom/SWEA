def move():
    global ans
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append((0, 0, 1, 1))  # y, x, 거리, 기회
    visited[0][0] = True

    while q:
        y, x, distance, chance = q.popleft()

        if y == N - 1 and x == M - 1:
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
                if chance == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx, distance + 1, chance))
                    visited_broken[ny][nx] = True
                elif chance == 0 and not visited_broken[ny][nx]:
                    visited_broken[ny][nx] = True
                    q.append((ny, nx, distance + 1, 0))
            else:
                if chance == 1 and not visited_broken[ny][nx]:
                    q.append((ny, nx, distance + 1, 0))
                    visited_broken[ny][nx] = True

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

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
