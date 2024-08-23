'''
1. 이동한다.
냄새가 없다면, 인덱스를 벗어나지 않았다면
갈 곳이 없다면 순회를 돌고 없다면 자신의 이전 냄새가 있는 곳으로 이동한다.
만약 자신의 냄새가 여러개라면 우선순위에 따라 움직인다!
2. 이동한 뒤 좌표를 모두 담는다.
같은 좌표가 있다면 번호가 작은 숫자를 지운다

+ 큰 숫자부터 이동하면 좋을 것 같다

3. 이동한 뒤 냄새를 남긴다.
'''

dx = [0, 0, -1, 1] # 1 2 3 4 = 위 아래 왼쪽 오른쪽
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())


sea = [list(map(int, input().split())) for _ in range(n)]

direc = list(map(int, input().split())) # 상어가 몇번째 우선순위를 갖는지에 대해
direc_list = [list(map(int, input().split())) for _ in range(m*4)] #전체 리스트

a = 0
shark_direc = [[]for _ in range(m)]
# 상어 인덱스별로 우선순위를 담아놓았다. 0번째가 1번 상어임에 주의
for i in range(m):
    a += direc[i]
    shark_direc[i].append(direc_list[a-1])

smell = [[[0,0] for _ in range(n)] for _ in range(n)]

def move(num, y, x):
    is_move = False
    direc_list = shark_direc[num-1] # 인덱스 순서
    for d in direc_list:
        ny = y + dy[d]
        nx = x + dx[d]
        if not(0 <= ny < n and 0 <= nx < n):
            continue
        if smell[ny][nx][0] != 0:
            continue
        if sea[ny][nx] == 0:
            sea[ny][nx] = num



# 처음 상어 위치를 갱신 + 냄새도 갱신
shark = [[] for _ in range(m)]
for y in range(n):
    for x in range(n):
        if sea[y][x] != 0:
            shark.append([sea[y][x], y, x])
            smell[y][x][0] = sea[y][x]
            smell[y][x][1] = k

s = 0
while True:
    if s >= 1000:
        break
    if len(shark) == 1:
        break
    shark.sort(reverse=True)
    for num, y, x in shark:
        move(num, y, x)