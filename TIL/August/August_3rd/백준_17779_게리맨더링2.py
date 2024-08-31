'''

1. 5를 먼저 채운다.
2. 맨 위 꼭짓점 좌표를 구한다
3. y - 1한 좌표부터 양쪽을 델타 탐색하며 5라면 그걸 5로 색칠하고 양쪽으로 보내서 BFS탐색

다른 방법

테두리
1
2
3
4 하고 나머지 5로 채워
'''
from collections import deque
from copy import deepcopy
import itertools

dx = [1, 1, -1, -1]  # 대각 우상 대각 우하 대각 좌하 좌상
dy = [-1, 1, 1, -1]

dx_bfs = [1, -1, 0, 0]
dy_bfs = [0, 0, 1, -1]
def bfs(y, x, arr):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([y, x])
    visited[y][x] = 1
    while q:
        ty, tx = q.popleft()
        for i in range(4):
            ny = ty + dy_bfs[i]
            nx = tx + dx_bfs[i]
            if arr[ny][nx] ==0 and visited[ny][nx] != 1:
                arr[ny][nx] = 5
                q.append((ny, nx))
def divide_city(y, x, arr, d1, d2):
    dir = 0
    arr[y][x] = 5

    for i in range(d1):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            arr[ny][nx] = 5
            y, x = ny, nx
        else:
            break
    dir += 1
    for i in range(d2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            arr[ny][nx] = 5
            y, x = ny, nx
        else:
            break
    for i in range(d1):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            arr[ny][nx] = 5
            y, x = ny, nx
        else:
            break
    for i in range(d2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            arr[ny][nx] = 5
            y, x = ny, nx
        else:
            break
    return arr
def fill_one(y, x, arr, d1):
    for ny in range(x+d1):
        for nx in range(y+1-ny):
            arr[ny][nx] = 1
    return arr
def fill_two(y, x, arr, d2):
    for ny in range(x+d2+1):
        for nx in range(n-y-2, -1, -1):
            if arr[ny][nx] != 0:
                break
            else:
                arr[ny][nx] = 2
    return arr
def fill_three(y, x, arr, d1, d2):
    for ny in range(x+d1,n):
        for nx in range(y-d1+d2):
            if arr[ny][nx] != 0:
                break
            else:
                arr[ny][nx] = 3
def fill_four(arr):
    for ny in range(n):
        for nx in range(n):
            if arr[ny][nx] == 0:
                arr[ny][nx] = 4

def get_spot(y, x):
    res = []
    for d1 in range(n):
        for d2 in range(n):
            if x+d1+d2 < n and y-d1 >= 0:
                pass
n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

for y in range(n):
    for x in range(n):
        pass
