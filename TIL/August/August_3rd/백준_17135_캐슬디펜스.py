import itertools
import copy
from collections import deque
n, m, d = map(int, input().split())#n이 y축
castle = [list(map(int, input().split())) for _ in range(n)]


a = [i for i in range(m)]
position = list(itertools.combinations(a, 3))

def calculate(pos, c):
    global cnt
    kill = set()
    for p in pos:
        target = (-1, -1)
        min_dist = d + 1

        for y in range(n-1, -1, -1):
            for x in range(m):
                if c[y][x] == 1:
                    dist = abs(y-n) + abs(p-x)
                    if dist <= d:
                        if dist < min_dist or (dist == min_dist and target[1] > x):
                            min_dist = dist
                            target = (y, x)
        if target != (-1, -1):
            kill.add(target)
    for y, x in kill:
        if c[y][x] == 1:
            c[y][x] = 0
            cnt += 1

cnt = 0
maximum = 0
for p in position:
    cnt = 0
    c = copy.deepcopy(castle)
    for tc in range(n):
        calculate(p, c)
        c.pop()
        c.insert(0, [0 for _ in range(m)])
    maximum = max(cnt, maximum)

print(maximum)
