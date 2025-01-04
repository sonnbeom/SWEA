# 0은 흰색, 1은 빨간색, 2는 파란색
# 아예 무빙이 없는 경우도 불가능이다.

def get_reverse_num(idx):
    if idx == 0:
        return 1
    elif idx == 1:
        return 0
    elif idx == 2:
        return 3
    else:
        return 2
def check_range(ny, nx):
    if not(0 <= nx < n and 0 <= ny < n):
        return False
    else:
        return True
def move(y, x, idx, horse):
    num = horse[idx]
    ny = y + dy[num]
    nx = x + dx[num]
    if not check_range(ny, nx):
        num = get_reverse_num(num)
        ny = y + dy[num]
        nx = x + dx[num]
        if not check_range(ny, nx):
            return
    elif chess[ny][nx] == 0:




def func(y, x):
    horse = horses[y][x]
    if len(horse) >= 4:
        return False
    small = min(horse)
    idx = horse.index(small)
    move(y, x, idx, horse)
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
checked = [False for _ in range(k)]
while True:
    cnt += 1
    for y in range(n):
        for x in range(n):
            if horses:
                res = func(y, x)
                if not res:
                    break



    if cnt > 1000:
        cnt = -1
        break
