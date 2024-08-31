import itertools
from copy import deepcopy
dx = [1, 0, -1, 0] # 동남서북
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

rotation_list = [list(map(int, input().split())) for _ in range(k)]

permutation = list(itertools.permutations(rotation_list, k))
min_count = int(1e9)

print(permutation)
for permu in permutation:
    cop_arr = deepcopy(arr)
    for r, c, s in permu:

        for i in range(s):
            top_y = r-s+i-1
            top_x = c-s+i-1
            bottom_y = r+s-1-i
            bottom_x = c+s-1-i
            y, x = top_y, top_x
            prev = cop_arr[y][x]
            for dir in range(4):
                while True:
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if top_x <= nx <= bottom_x and top_y <= ny <= bottom_y:
                        tmp = cop_arr[ny][nx]
                        cop_arr[ny][nx] = prev
                        prev = tmp
                        y, x = ny, nx
                    else:
                        break
    for y in cop_arr:
        min_count = min(min_count, sum(y))
print(min_count)


