t = int(input())
for testCase in range(1, t+1):
    def getVisitedList():
        visited = [False for _ in range(10)]
        visited[0] = True
        return visited
    def isSdk(req):
        if False in req:
            return 1
        else:
            return 0
    def isSdRec(reqList, y, x):
        visited = getVisitedList()
        for dy in range(3):
            nowY = dy + y
            for dx in range(3):
                nowX = x + dx
                temp = reqList[nowY][nowX]
                visited[temp] = True
        return visited

    def isSdGaro(reqList, y, x):
        visited = getVisitedList()
        for dx in range(9):
            nowX = x + dx
            temp = reqList[y][nowX]
            visited[temp] = True
        return visited

    def isSdSero(reqList, y, x):
        visited = getVisitedList()
        for dy in range(9):
            nowY = y + dy
            temp = reqList[nowY][x]
            visited[temp] = True
        return visited
    res = 0
    arr = [list(map(int, input().split())) for _ in range(9)]
    recCheck = [0, 3, 6]

    res = 1
    for i in range(9):
        if i in recCheck:
            for j in recCheck:
                resSdRec = isSdRec(arr ,i, j)
                res += isSdk(resSdRec)
        resSero = isSdSero(arr, 0, i)
        res += isSdk(resSero)
        resGaro = isSdGaro(arr, i, 0)
        res += isSdk(resGaro)

    if res == 1:
        print(f'#{testCase} {res}')
    else:
        print(f'#{testCase} 0')