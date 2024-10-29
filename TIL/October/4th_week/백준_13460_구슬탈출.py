from collections import deque

def bfs(sy, sx):
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = 11
    q = ()
    deque.append((sy, sx, 0))

    while q:
        y, x, cnt = q.popleft()

        if cnt > 10:
            continue
        for i in range(4):
            ty = y
            tx = x
            while True:
                ny = ty + dy[i]
                nx = tx + dx[i]
                if not(1 <= ny < n-1 and 1 <= nx < m):
                    break
                if visited[ny][nx]:
                    break
                if arr[ny][nx]:
                    pass

dx = [0, 0, -1, 1]
dy = [1, -1, 1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

