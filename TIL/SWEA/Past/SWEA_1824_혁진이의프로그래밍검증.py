r, c = map(int, input().split())
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]
# 우 좌 하 상
direc = 0
# visited = [False for _ in range(16)]
# 메모리, 방향을 담자 메모리와 방향이 같다면 오류 배열에는 [메모리][방향] = (위치)
visited = [[[] for _ in range(c)] for _ in range(r)]
memory = 0
numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def direcChange(req):
    global direc
    if req == '<':
        direc = 1
    elif req == '>':
        direc = 0
    elif req == '^':
        direc = 3
    else:
        direc = 2
def memoryChange(req):
    global memory
    global direc
    if req == '+':
        if memory == 15:
            memory = 0
        else:
            memory += 1
    elif req == '-':
        if memory == 0:
            memory = 15
        else: memory -= 1
    elif req == '_':
        if memory == 0:
            direc = 0
        else:
            direc = 1
    else:
        if memory == 0:
            direc = 2
        else:
            direc = 3
def al(req):
    if req == '.':
        pass
def decide(req):
    global memory
    if req in ['>', '<', '^', 'v']:
        direcChange(req)
    elif req in ['+', '-', '_', '|']:
        memoryChange(req)
    elif req == '.':
        pass
    elif req in numList:
        memory = int(req)

arr = [list(input()) for _ in range(r)]

res = 'NO'

def check():
    res = False
    for i in range(r):
        if '@' in arr[i]:
           res = True
           return res
    return res

def rangeCheckX(x):
    if x < 0:
        return c-1
    elif x >= c:
        return 0
    else:
        return x
def rangeCheckY(y):
    if y < 0:
        return r-1
    elif y >= r:
        return 0
    else:
        return y
def func():
    global direc
    q = [(0, -1, 0)]
    while q:
        y, x, dir = q.pop()
        # y, x, dir = q.pop(0)
        direc = dir
        nowX = x + dx[dir]
        nowY = y + dy[dir]
        nowX = rangeCheckX(nowX)
        nowY = rangeCheckY(nowY)
        
        temp = arr[nowY][nowX]
        if temp == '@':
            q.clear()
            return 'YES'
        if temp == '?':
            if (memory, direc) in visited[nowY][nowX]:
                q.clear()
                return "NO"
            else:
                visited[nowY][nowX].append((memory, dir))
            for i in range(4):
                #왔던 방향은 제거 인덱스 체크
                qX = nowX + dx[i]
                qX = rangeCheckX(qX)
                qY = nowY + dy[i]
                qY = rangeCheckY(qY)
                
                if y != qY or x != qX:
                    q.append((nowY, nowX, i))
                    # q.insert(0, (nowY, nowX, i))

                # 여기에 visited에 확인, 넣고 q.append(nowY,nowY)
        else:
            decide(temp)
            dir = direc
            if visited[nowY][nowX].count((memory, dir)) >= 2:
                q.clear()
                return "NO"
            visited[nowY][nowX].append((memory, dir))
            q.append((nowY, nowX, dir))

can = check()
if can:
    res = func()
else:
    res = "NO"
print(res)
    
