# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
'''
00 01
10 11

'''
t = 0
def b(d):
    if d == 0:
        return 2
    elif d == 2:
        return 0
    elif d == 1:
        return 3
    else:
        return 1
    
def check(y, x):
    for i in range(4):
        nowX = x + dx[i]
        nowY = y + dy[i]
        if 0 <= nowX < m and 0 <= nowY < n:
            if room[nowY][nowX] == 0 and visited[nowY][nowX] == 0:
                return True
    return False

def getSpot(y, x, d):
    d = (d+3) % 4
    # d = (d+1) % 4
    for i in range(4):
        nowX = x + dx[d]
        nowY = y + dy[d]
        if room[nowY][nowX] == 0 and visited[nowY][nowX] == 0:
            return (nowY, nowX, d)
        d = (d+3) % 4
        # d = (d+1) % 4

def solution(y, x, d):
    global t 
    if room[y][x] == 0 and visited[y][x] == 0:
        visited[y][x] = 1 
        t += 1
    noEmpty = check(y,x)
    if noEmpty:
        nY, nX, nD = getSpot(y,x,d)
        solution(nY, nX, nD)
    else:
        dir = b(d)
        nowX = dx[dir] + x
        nowY = dy[dir] + y
        if 0 <= nowY < n and 0 <= nowX < m and room[nowY][nowX] == 0:
            solution(nowY, nowX , d)

n, m = map(int, input().split())
y, x, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

solution(y, x, d)

print(t)