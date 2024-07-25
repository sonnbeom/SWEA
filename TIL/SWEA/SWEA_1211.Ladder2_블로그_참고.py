arr = [list(map(int, input().split())) for _ in range(100)]

startList = []
for i in range(100):
    if arr[0][i] == 1:
        startList.append(i)

def findDistance(start):
    x = start
    y = 0
    count = 0

    while y != 99:
        if 0 < x-1 and arr[y][x-1] == 1:
            while 0 < x-1 and arr[y][x-1] == 1:
                x -= 1
                count += 1 
        elif 100 > x+1 and arr[y][x+1] == 1:
            while 100 > x+1 and arr[y][x+1] == 1:
                x += 1
                count += 1
        y += 1
    
    return count

countList = []
for i in startList:
    countList.append(findDistance(i))
res = startList[countList.index(min(countList))]