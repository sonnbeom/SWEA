'''

필요한 기능
1. 이동한다.
냄새가 없다면, 인덱스를 벗어나지 않았다면
현재 방향에 기반해 움직일 곳을 찾는다.
갈 곳이 없다면 순회를 돌고 없다면 자신의 이전 냄새가 있는 곳으로 이동한다.
만약 움직였다면 우선순위를 바꿔주나

만약 잡아먹을 경우
바다 내에서 해당 숫자를 대체
상어를 삭제
방문 배열에서도 해당 내용을 업데이트

2. 이동한 뒤 해야할 것들
상어 좌표를 담자(번호, y좌표, x좌표, 바라보고있는 방향)
바다에 있는 상어 좌표도 바꾸자
방문 배열에 상어의 번호
냄새 크기(=k)를 넣는다 [1, 4]

3. 초를 체크한다. 1000초가 넘어가면 브레이크
4. 만약 상어의 사이즈가 하나라면 브레이크
+ 큰 숫자부터 이동하면 좋을 것 같다

3. 이동한 뒤 냄새를 남긴다.

1 = 위
2 = 아래
3 = 왼쪽
4 = 오른쪽
4 3 1 2 => dx dy 순서도 맞춰야 한다
00 01
10 11
[
    [
        [1,2],
        [2,3]
    ]
]

'''
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 현재 방향에 기반해 상어가 바라봐야할 우선 순위를 제공
def decide_direction(num, dir):
    return direction_list[num - 1][dir - 1]

def create_smell():
    for s in shark:
        num = s[0]
        y = s[1]
        x = s[2]
        visited[y][x][0] = num
        visited[y][x][1] = K

def update_smell(visited_update):
    if not (len(visited_update) > 0):
        return
    for li in visited_update:
        y, x = li[0], li[1]
        visited[y][x][1] = K
def kill_weak_shark():
    if len(weak_shark_list) == 0:
        return
    for sh in shark.copy():
        if sh[0] in weak_shark_list:
            shark.remove(sh)

def minus_smell():
    for y in range(N):
        for x in range(N):
            if visited[y][x][1] > 1:
                visited[y][x][1] -= 1
            elif visited[y][x][1] == 1:
                visited[y][x][0] = 0
                visited[y][x][1] = 0

def move(idx, num, y, x, dir):
    go = 0
    for d in dir:
        ny = y + dy[d - 1]
        nx = x + dx[d - 1]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx][0] == 0:  # 빈 칸만 차지한다.
                if sea[ny][nx] == 0:
                    shark[idx][1] = ny
                    shark[idx][2] = nx
                    shark[idx][3] = d
                    sea[ny][nx] = num
                    sea[y][x] = 0
                    go += 1
                    break
                elif sea[ny][nx] != 0:  # 잡아 먹는다
                    tmp = sea[ny][nx]
                    sea[ny][nx] = num
                    weak_shark_list.append(tmp)
                    shark[idx][1] = ny
                    shark[idx][2] = nx
                    shark[idx][3] = d
                    sea[y][x] = 0
                    go += 1
                    break
    if go == 0:
        for d in dir:
            ny = y + dy[d - 1]
            nx = x + dx[d - 1]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx][0] == num:
                    shark[idx][1] = ny
                    shark[idx][2] = nx
                    shark[idx][3] = d
                    sea[ny][nx] = num
                    sea[y][x] = 0
                    visited_update.append([y, x]) # 상어 숫자 y, x움직이고 다 줄이고 냄새 있는 곳으로 갔다면 다시 갱신해야 하므로
                    break

N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
# 상어별로 처음 우선순위
direction = list(map(int, input().split()))
# 상어 번호별로 방향 우선순위 1번 상어: 0번 2번 상어: 1번 and...
direction_list = []
visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
for i in range(M):
    tmp = []
    for j in range(4):
        d_list = list(map(int, input().split()))
        tmp.append(d_list)
    direction_list.append(tmp)

# 번호, y좌표, x좌표, 바라보고있는 방향
shark = []
visited_update= []
weak_shark_list = []
for y in range(N):
    for x in range(N):
        if sea[y][x] != 0:
            tmp = [sea[y][x], y, x, direction[sea[y][x] - 1]]
            shark.append(tmp)
            visited[y][x][0] = sea[y][x]
            visited[y][x][1] = K

second = 0
while True:
    if len(shark) == 1:
        print(second)
        break
    if second > 1000:
        print(-1)
        break
    second += 1
    shark.sort(reverse=True)

    visited_update = []
    weak_shark_list = []
    print(visited)
    for i in range(len(shark)):
        s = shark[i]
        d = decide_direction(s[0], s[-1])
        move(i, s[0], s[1], s[2], d)
    kill_weak_shark()
    minus_smell()
    create_smell()
    update_smell(visited_update)
