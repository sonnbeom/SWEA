t = int(input())
for testCase in range(1, t+1):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    direc = 0
    i = 2
    y = 0
    x = 0
    arr[0][0] = 1
    while i < n*n+1:
        nowX = x + dx[direc]
        nowY = y + dy[direc]
        if 0<= nowX < n and 0<= nowY < n and arr[nowY][nowX] == 0:
            arr[nowY][nowX] = i
            x = nowX
            y = nowY
            i += 1
        else:
            direc = (direc+1) % 4
            

    print(f'#{testCase}')
    for i in range(n):
        print(*arr[i])