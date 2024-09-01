'''

1번 좌 우 상 하
2번 좌 우, 상 하
3번 상 우 상 좌 하 우 하 좌
4번 한 방향 제외
5번 전부 다

1번 => 0 1 2 3
2번 => 01, 23
3번 => 12, 02, 13, 03
4번 => 012, 013, 123, 023

'''
# 좌 우 상 하


'''

dfs 
2차원 배열을 돌며 1이면 1에 해당하는 배열을 넣고
2라면 2에 해당하는 배열을 넣는다.
ex) [[0,1,2,3] [[0,1], [2,3]]

1. 깊이가 n이 되면 리턴

2. 단일인 경우도 있고 배열도 있잖아요 만약 길이가 1이라면 그냥 bfs 돌리고 아니라면
for문을 돌려서 bfs 돌리면 된다.

+ 최소 크기를 구해야 하므로 가장 큰 좌표부터 돌리고 만약 미니멀 숫자보다 크다면 break or return 
3번 => 12, 02, 13, 03
4번 => 012, 013, 123, 023
'''
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

trial_list =[]

def dfs(idx ,depth, temp_arr):
    if depth == length:
        trial_list.append(temp_arr.copy())
        return

    arr_len = len(dfs_list[idx])
    for i in range(arr_len):
        node = dfs_list[idx][i]
        if not visited[idx][i]:
            temp_arr.append(node)
            visited[idx][i] = True
            dfs(idx+1, depth+1, temp_arr)
            visited[idx][i] = False
            temp_arr.pop()
def bfs(y, x, temp, trial, current_min):
    # if current_min >= minimum:
    #     return
    if type(trial) == int:
        temp[y][x] = 1
        current_min += 1
        while True:
            nx = x + dx[trial]
            ny = y + dy[trial]
            if not (0 <= nx < m and 0 <= ny < n):
                break
            if temp[ny][nx] == 2:
                break
            temp[ny][nx] = 1
            current_min += 1
            y = ny
            x = nx
    else:
        temp[y][x] = 1
        current_min += 1
        o_y = y
        o_x = x
        for idx in trial:
            y = o_y
            x = o_x
            while True:
                # if current_min >= minimum:
                #     return
                nx = x + dx[idx]
                ny = y + dy[idx]
                if not(0 <= nx < m and 0 <= ny < n):
                    break
                if temp[ny][nx] == 2:
                    break
                temp[ny][nx] = 1
                current_min += 1
                y = ny
                x = nx


def bfs_five(y, x, temp, current_min):

    temp[y][x] = 1
    current_min += 1
    o_x = x
    o_y = y
    for i in range(4):
        y = o_y
        x = o_x
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < m and 0 <= ny < n):
                break
            if temp[ny][nx] == 2:
                break
            temp[ny][nx] = 1
            current_min += 1
            y = ny
            x = nx



def append_visited(arr_len):
    v = [False for _ in range(arr_len)]
    visited.append(v)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

one = [0, 1, 2, 3]
two = [[0, 1], [2, 3]]
three = [[1, 2], [0, 2], [1, 3], [0, 3]]
four = [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]]
five = [5]

start_position = []
wall = []
dfs_list = []
visited = []
visited_bfs = [[False for _ in range(m)] for _ in range(n)]
for y in range(n):
    for x in range(m):
        if arr[y][x] != 0 and arr[y][x] != 6:
            start_position.append([y, x])
            if arr[y][x] == 1:
                dfs_list.append(one)
                append_visited(len(one))
            elif arr[y][x] == 2:
                dfs_list.append(two)
                append_visited(len(two))
            elif arr[y][x] == 3:
                dfs_list.append(three)
                append_visited(len(three))
            elif arr[y][x] == 4:
                dfs_list.append(four)
                append_visited(len(four))
            else:
                dfs_list.append(five)
                append_visited(len(five))
        elif arr[y][x] == 6:
            wall.append([y, x])
length = len(start_position)

dfs(0, 0, [])


minimum = int(1e9)
wall_cnt = len(wall)
square_cnt = n * m
max_cnt = square_cnt - wall_cnt

for trial in trial_list:
    arr_temp = [[0 for _ in range(m)] for _ in range(n)]
    for y, x in wall:
        arr_temp[y][x] = 2
    idx = 0
    current = max_cnt
    current_min = 0
    for t in trial:
        if t != 5:
            bfs(start_position[idx][0], start_position[idx][1], arr_temp, t, current_min)
        elif t == 5:
            bfs_five(start_position[idx][0], start_position[idx][1], arr_temp, current_min)
        idx += 1


    cnt = 0
    for i in range(n):
        cnt += arr_temp[i].count(0)
        if cnt >= minimum:
            break
    minimum = min(minimum, cnt)
print(minimum)
