for _ in range(10):
    testCase = int(input())
    startX = 0 
    startY = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                startY = i
                startX = j
    res = 0

    def dfs(y, x):
        global res
        arr[y][x] = 1
        for i in range(4):
            nowX = x + dx[i]
            nowY = y + dy[i]
            if arr[nowY][nowX] == 3:
                res = 1
                return
            if 0 <= nowY < 16 and 0 <= nowX < 16 and arr[nowY][nowX] == 0:
                dfs(nowY, nowX)
        return res
    
    print(f'#{testCase} {dfs(startY, startX)}')

