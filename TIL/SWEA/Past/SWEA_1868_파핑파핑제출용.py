t = int(input())
for tc in range(1, t+1):
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
    for y in range(n):
        for x in range(n):
            if arr[y][x] == '.' and visited[y][x] == False:
                bfs(y, x) 

    print(f'#{tc} {resCount}')