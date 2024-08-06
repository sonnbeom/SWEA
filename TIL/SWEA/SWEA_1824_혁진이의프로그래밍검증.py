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

res = ''

def check():
    res = False
    for i in range(c):
        if '@' in arr[i]:
           res = True
           return res
    return res
def func(y, x):
    # go = True
    # while go:
    global res
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
        res = 'YES'
        return
    if temp == '?':
        for i in range(4):
            qX = nowX + dx[i]
            qY = nowY + dy[i]
            func(qY, qX)
    decide(temp)
    if (memory, direc) in visited[nowY][nowX]:
        return
    visited[nowY][nowX].append((memory, direc))
    func(nowY, nowX)

can = check()
if can:
    func(0, -1)
# else:
#     res = "NO"

print(res)
    
