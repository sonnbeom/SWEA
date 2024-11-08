from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    visited = [[(100*100) for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0
    q.append((0, 0, 0))
    while q:
        y, x, cnt = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 인덱스 벗어나는지 체크
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            # miro 값이 1이라면 cnt에 1을 더하고 방문 배열 값과 비교한다.
            if miro[ny][nx] == 1:
                new_cnt = cnt + 1
            # miro 값이 0이라면 그대로
            elif miro[ny][nx] == 0:
                new_cnt = cnt
            # 방문하려는 곳과 비교, 더 작다면 최소 횟수로 미로를 부신 것이므로 queue에 담는다.
            if new_cnt < visited[ny][nx]:
                visited[ny][nx] = new_cnt
                q.append((ny, nx, new_cnt))

    return visited[N-1][M-1]

M, N = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

print(bfs())
