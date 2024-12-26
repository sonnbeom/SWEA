from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
answer = int(1e9)


def get_outline(arr, my, mx):
    outline = []
    q = deque()
    q.append((0, 0))
    if arr[0][0] != 0:
        outline.append((0, 0))
    visited = [[False for _ in range(mx)] for _ in range(my)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < mx and 0 <= ny < my):
                continue
            elif visited[ny][nx]:
                continue
            elif arr[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = True
            elif arr[ny][nx] != 0:
                outline.append((ny, nx))
                visited[ny][nx] = True
    return outline


def make_arr(rectangle):
    arr_y = 0
    arr_x = 0
    for sx, sy, bx, by in rectangle:
        arr_y = max(by, arr_y)
        arr_x = max(bx, arr_x)

    arr = [[0 for _ in range(arr_x + 2)] for _ in range(arr_y + 2)]
    for sx, sy, bx, by in rectangle:
        for y in range(by, sy - 1, -1):
            for x in range(sx, bx + 1):
                arr[y][x] += 1
    return arr


def draw(outline, arr):
    for y, x in outline:
        arr[y][x] = True
    return arr


def get_distance(graph, y, x, ty, tx, d, visited, my, mx):
    global answer
    if d >= answer:
        return
    elif y == ty and x == tx:
        answer = min(answer, d)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= nx < mx and 0 <= ny < my):
            continue
        if graph[ny][nx]:
            visited[ny][nx] = True
            get_distance(graph, ny, nx, ty, tx, d + 1, visited, my, mx)
            visited[ny][nx] = False


def solution(rectangle, sx, sy, tx, ty):
    arr = make_arr(rectangle)
    outline = get_outline(arr, len(arr), len(arr[0]))
    empty_graph = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    graph = draw(outline, empty_graph)
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    get_distance(graph, sy, sx, ty, tx, 0, visited, len(arr), len(arr[0]))
    print(answer)
    return answer
