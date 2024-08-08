'''
함수 2개
1. 함수 주변 지뢰 몇개?
2. 0이 있다? 재귀 ㄱㄱ
3. 주변에 .이 최대 몇개 있는지 체크
4. 그 좌표로 계속 갱신하는 거지


00 01 02
10 11 12
20 21 22

좌 우 상 하 대각 좌상 우상 좌하 우하
0 1 2 3 4 5 6 7 8
'''

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
n = int(input())
arr = [list(input()) for _ in range(n)]
resCount = 0
visited = [[False for _ in range(n)] for _ in range(n) ]


def bfs(y, x):
    q = [(y,x)]
    global resCount
    while q:
        tempY, tempX = q.pop(0)
        tmpCount = 0
        tmp = True
        recurList = []
        for i in range(8):
            nowX = tempX + dx[i]
            nowY = tempY + dy[i]
            if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] == '*' and visited[nowY][nowX] == False:
                tmp = False
                tmpCount += 1
        if tmp == False:
            arr[tempY][tempX] = tmpCount
            visited[tempY][tempX] = True
            if y == tempY and x == tempX:
                resCount += 1
        else:
            arr[tempY][tempX] = 0
            visited[tempY][tempX] = True
            for i in range(8):
                nowX = tempX + dx[i]
                nowY = tempY + dy[i]
                if 0 <= nowX < n and 0 <= nowY < n and visited[nowY][nowX] == False:
                    arr[nowY][nowX] = 0
                    if (nowY, nowX) not in q:
                        recurList.append((nowY, nowX))
            if y == tempY and x == tempX:
                resCount += 1
        if len(recurList) > 0:
            for rY, rX in recurList:
                q.append((rY, rX))
            
def getZeroMax():
    zeroList = []
    for y in range(n):
        for x in range(n):
            if arr[y][x] == '.':
                temp = True
                for i in range(8):
                    nowX = x + dx[i]
                    nowY = y + dy[i]
                    if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] != '.':
                        temp = False
                if temp == True:
                    zeroList.append((y,x))
    return zeroList

zeroList = getZeroMax()

if len(zeroList) > 0:
    for y, x in zeroList:
        if arr[y][x] == '.' and visited[y][x] == False:
            bfs(y, x)
print(*zeroList)
for y in range(n):
    for x in range(n):
        if arr[y][x] == '.' and visited[y][x] == False:
            bfs(y, x) 

print(resCount)



# def getCount(y, x, cnt):
#     global resCount
#     recurList = []
#     tmp = True
#     tmpCount = 0
#     for i in range(8):
#         nowX = x + dx[i]
#         nowY = y + dy[i]
#         if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] == '*':
#             tmp = False
#             tmpCount += 1
#     if tmp == False:
#         arr[y][x] = tmpCount
#         if cnt == 0:
#             resCount += 1
#     else:
#         arr[y][x] = 0
#         for i in range(8):
#             nowX = x + dx[i]
#             nowY = y + dy[i]
#             if 0 <= nowX < n and 0 <= nowY < n:
#                 arr[nowY][nowX] = 0
#                 recurList.append((nowY, nowX))
#         if cnt == 0:
#             resCount += 1   
#     for zY, zX in recurList:
#         getCount(zY, zX, cnt +1)