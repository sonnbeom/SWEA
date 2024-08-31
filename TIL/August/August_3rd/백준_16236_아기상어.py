from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]


def bfs(y, x, size):
    q = deque([(y, x, 0)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    candidates = []
    min_dist = float('inf')

    while q:
        cy, cx, dist = q.popleft()

        # 만약 이미 찾은 최단 거리보다 멀면 탐색을 종료
        if dist > min_dist:
            break

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if sea[ny][nx] <= size:
                    visited[ny][nx] = True
                    if 0 < sea[ny][nx] < size:
                        min_dist = dist + 1
                        candidates.append((min_dist, ny, nx))
                    q.append((ny, nx, dist + 1))

    if candidates:
        # 거리, y, x 순으로 정렬하여 가장 최적의 위치 선택
        candidates.sort()
        return candidates[0]
    else:
        return None


size = 2
size_up = 0
cnt = 0
shark = [-1, -1]

# 상어 위치 초기화
for y in range(n):
    for x in range(n):
        if sea[y][x] == 9:
            shark = [y, x]
            sea[y][x] = 0  # 상어가 있던 자리는 0으로 초기화

while True:
    result = bfs(shark[0], shark[1], size)

    if not result:
        break

    dist, shark_y, shark_x = result
    cnt += dist
    size_up += 1

    # 상어 위치 갱신
    shark[0] = shark_y
    shark[1] = shark_x

    # 먹은 물고기의 위치를 0으로 초기화
    sea[shark_y][shark_x] = 0

    # 상어의 크기 증가 조건 체크
    if size_up == size:
        size += 1
        size_up = 0

print(cnt)
