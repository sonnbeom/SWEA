from collections import deque
import sys


sys.setrecursionlimit(10 ** 8)
answer =100
dx = [0, 0, -1, 1] # 하 상 좌 우
dy = [1, -1, 0, 0]

ddx = [-1, 1, -1, 1]
ddy = [-1, -1, 1, 1]
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
    l = max(arr_y, arr_x)
    arr = [[0 for _ in range(arr_x)] for _ in range(arr_y)]
    for sx, sy, bx, by in rectangle:
        for y in range(by - 1, sy - 1, -1):
            for x in range(sx, bx):
                arr[y][x] += 1
    return arr


def draw(outline, arr):
    for y, x in outline:
        arr[y][x] = 1
    return arr
def fill(graph):
    len_y = len(graph)
    lex_x = len(graph[0])
    check = [[False for _ in range(lex_x)] for _ in range(len_y)]
    pass



def get_distance(graph, y, x, ty, tx, d, visited, my, mx):
    global answer
    if d >= answer:
        return
    elif abs(ty - y) == 1 and abs(tx - x) == 1:
        answer = min(answer, d + 2)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= nx < mx and 0 <= ny < my):
            continue
        elif visited[ny][nx]:
            continue
        elif not graph[ny][nx]:
            continue
        elif graph[ny][nx]:
            visited[ny][nx] = True
            get_distance(graph, ny, nx, ty, tx, d + 1, visited, my, mx)
            visited[ny][nx] = False
        ny = y + ddy[i]
        nx = x + ddx[i]
        if not (0 <= nx < mx and 0 <= ny < my):
            continue
        elif visited[ny][nx]:
            continue
        elif not graph[ny][nx]:
            continue
        elif graph[ny][nx]:
            visited[ny][nx] = True
            get_distance(graph, ny, nx, ty, tx, d + 2, visited, my, mx)
            visited[ny][nx] = False
def bfs(graph, sy, sx, ty, tx):
    res = 100
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[sy][sx] = True
    q = deque()
    q.append((sy, sx, 0))
    len_y = len(graph)
    len_x = len(graph[0])
    while q:
        y, x, d = q.popleft()
        print(f'y = {y} x ={x} d ={d}')
        if d >= res:
            print(f' res = {res} d = {d}')
            continue
        elif abs(ty - y) == 1 and abs(tx - x) == 1:
            print(f'여기 언제옴? y = {y} x ={x} ty ={ty} tx ={tx} d={d}')
            res = min(res, d + 2)
        for i in range(4):
            ny = y +dy[i]
            nx = x +dx[i]
            if not(0 <= ny < len_y and 0 <= nx < len_x):
                continue
            elif visited[ny][nx]:
                continue
            elif not graph[ny][nx]:
                continue
            elif graph[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, d+1))
        for i in range(4):
            ny = y + ddy[i]
            nx = x + ddx[i]
            if not (0 <= ny < len_y and 0 <= nx < len_x):
                continue
            elif visited[ny][nx]:
                continue
            elif not graph[ny][nx]:
                continue
            elif graph[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, d+2))
    return res
def bfs_arr(arr, sy, sx, ty, tx):
    response = 1000
    visited = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    visited[sy][sx] = True
    q = deque()
    q.append((sy, sx, 0))
    len_y = len(arr)
    len_x = len(arr[0])

    while q:
        y, x, d = q.popleft()

def solution(rectangle, sx, sy, tx, ty):
    arr = make_arr(rectangle)
    arr.reverse()
    for i in range(len(arr)):
        print(f'arr ={arr[i]}')
    outline = get_outline(arr, len(arr), len(arr[0]))
    empty_graph = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    graph = draw(outline, empty_graph)
    # graph.reverse()
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[sy][sx] = True
    sy = len(graph) - sy -1
    ty = len(graph) - ty -1
    for i in range(len(graph)):
        print(f'graph = {graph[i]}')
    print(f'sy = {sy} sx = {sx} ty ={ty} tx = {tx}')
    print(f'graph[sy][sx] = {graph[sy][sx]} graph[ty][[tx] = {graph[ty][tx]}')
    get_distance(graph, sy, sx, ty, tx, 0, visited, len(graph), len(graph[0]))
    print(f'dfs = {answer}')
    res = bfs(graph, sy, sx, ty, tx)
    res_v2 = bfs_arr(arr, sy, sx, ty, tx)
    print(f'bfs = {res}')
    return answer
solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)