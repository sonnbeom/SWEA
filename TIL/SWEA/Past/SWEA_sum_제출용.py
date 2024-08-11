for testCase in range(10):
    
    def getGaroMax(req, n, x):
        res = 0
        for i in range(n):
            res += req[i][x]
        return res

    def getSeroMax(req, n, y):
        res = 0
        for i in range(n):
            res += req[y][i]
        return res

    def getDiaLtoR(req, n):
        res = 0
        for i in range(n):
            res += req[i][i]
        return res
    def getDiaRtoL(req, n):
        res = 0
        for i in range(n):
            res += req[i][n-i-1]
        return res

    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    tempList = []

    #가로 최댓값
    for i in range(100):
        maxGaro = getGaroMax(arr, 100, i)
        tempList.append(maxGaro)
        maxSero = getSeroMax(arr, 100, i)
        tempList.append(maxSero)

    diaMaxLtoR = getDiaLtoR(arr, 100)
    tempList.append(diaMaxLtoR)

    diaMaxRtoL = getDiaRtoL(arr, 100)
    tempList.append(diaMaxRtoL)

    res = 0
    for sumMax in tempList:
        if sumMax > res:
            res = sumMax
            
    print(f'#{t} {res}')
