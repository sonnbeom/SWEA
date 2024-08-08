import random
'''

00 01
10 11
'''
r, c = map(int, input().split())
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]
# 우 좌 하 상
direc = 0
visited = [False for _ in range(16)]
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
def RandomDirec():
    global direc
    direc = random.randrange(0,4)
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
    elif req == '?':
        RandomDirec()
    elif req in numList:
        memory = int(req)

arr = [list(input()) for _ in range(r)]

# y = 0
# x = -1
# go = True
res = ''

def check():
    res = False
    for i in range(c):
        if '@' in arr[i]:
           res = True
           return res
    return res
def func():
    y = 0
    x = -1
    go = True
    while go:
        if False not in visited:
            return 'NO'
            break
        nowX = x + dx[direc]
        nowY = y + dy[direc]
        if 0 > nowY:
            nowY = r-1
        elif nowY >= r:
            nowY = 0
        elif nowX < 0:
            nowX = c-1
        elif nowX >= c:
            nowX = 0
        temp = arr[nowY][nowX]
        if temp == '@':
            return 'YES'
            break
        #이게 아니라 다른 방법인 듯 하다.
        '''
        .랑 ? 어떻게 처리할지 고민
        '''
        # if temp == '.':
        #     tmpX = nowX + dx[direc]
        #     tmpY = nowY + dy[direc]
        #     if arr[tmpY][tmpX] == '.':
        #         return 'NO'
        decide(temp)
        x = nowX
        y = nowY
        visited[memory] = True
can = check()
if can:
    res = func()
else:
    res = "NO"

print(res)
    
