t = int(input())
for t in range(1, t+1):
    def checkVisited(x, nowX, nowY):
        for i in range(x, nowX + 1):
            visited[nowY][i] = True

    def getSize(y, x):
        visited[y][x] = True 
        nowX = x
        nowY = y
        while 0 <= nowX +1 < n:
            if arr[y][nowX+1] != 0 and visited[y][nowX+1] == False:
                nowX += 1
                visited[y][nowX] = True
            else:
                break
        while 0 <= nowY +1 < n:
            if arr[nowY+1][x] != 0 and visited[nowY+1][x] == False:
                nowY += 1
                checkVisited(x, nowX, nowY)
            else:
                break
        garo = nowX - x + 1
        sero = nowY - y + 1
        return [garo * sero, sero, garo]

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for i in range(n)] for _ in range(n)]

    size = 0
    parentList = [[] for _ in range((n+1)*(n+1))]

    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and visited[i][j] == False:
                res =getSize(i, j)
                listChild = [res[1], res[2]]
                parentList[res[0]].append(listChild)
                count += 1
    print(f'#{t} {count}', end= ' ')
    for child_list in parentList:
        child_list.sort()
        for child in child_list:
            if child:
                print(child[0], child[1], end=' ')
    print()