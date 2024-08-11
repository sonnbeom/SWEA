n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def getFlyCount(reqList, y, x, m):
    res = 0
    for i in range(m):
        nowY = y + i
        for j in range(m):
            nowX = x + j
            res += reqList[nowY][nowX]
    return res

tempList = []
for y in range(n-m+1):
    for x in range(n-m+1):
        fly = getFlyCount(arr, y, x, m)
        tempList.append(fly) 
        
print(max(tempList))