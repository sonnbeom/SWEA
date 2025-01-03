# 0은 흰색, 1은 빨간색, 2는 파란색
from SWEA.TIL.SWEA.Past.SWEA_4408_자기방으로돌아가기 import small


def move(y, x):
    horse = horses[y][x]
    small_num = min(horse)
    pass
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, k = map(int, input().split())
chess = []
for _ in range(n):
    a = list(map(int, input().split()))
    chess.append(a)
horses = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(k):
    y, x, d = map(int, input().split())
    horses[y-1][x-1].append(d-1)
cnt = 0
while True:
    cnt += 1
    for y in range(n):
        for x in range(n):
            if horses:
                move(y, x)




    if cnt > 1000:
        cnt = -1
        break
