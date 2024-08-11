'''
배열 크기가 n*2 +2

함수르 만들자
가로 n번을 도는 함수인데 n번까지 더하고 시작점은 (0,0) (1, 0)...(99,0)
세로 n번을 도는 함수인데 n번을 더한다 (0, 0) (0, 1)....(0,99)
대각선 2 번을 돈다 위치는? 
00 11 22 33 44 55 (99,99)... 좌측에서 우측
0 99 1 98 2 97 .... (99, 0)... 우측에서 좌측

'''
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

r = 0

for sumMax in tempList:
    if sumMax > r:
        r = sumMax

print(r)
