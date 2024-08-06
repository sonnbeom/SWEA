t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    tempSum = 0 
    tempList = []
    def recur(y, x, start):
        global tempSum
        tempSum += 1
        visited[y][x] = True
        tempList.append((tempSum, start))
        for i in range(4):
            nowX = x + dx[i]
            nowY = y + dy[i]
            if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] == arr[y][x] +1 and visited[nowY][nowX] == False:
                recur(nowY, nowX, start)
                visited[nowY][nowX] = False

    for y in range(n):
        for x in range(n):
            recur(y, x, arr[y][x])
            tempSum = 0
            visited[y][x] = False

    tempList.sort()

    maxRoomCount = tempList[-1][0]
    start = tempList[-1][1]

    for roomCount, roomNum in tempList:
        if roomCount == maxRoomCount and start > roomNum:
            start = roomNum
    print(f'#{tc} {start} {maxRoomCount}')