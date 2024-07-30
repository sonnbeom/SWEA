t = int(input())
for testCase in range(1, t+1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    temp = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(y, x, req):
        req += arr[y][x]
        if len(req) == 7:
            temp.append(req)
            return
        for i in range(4):
            nowX = x + dx[i]
            nowY = y + dy[i]
            if 0 <= nowX < 4 and 0 <= nowY < 4:
                dfs(nowY, nowX, req)
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
    print(f'#{testCase} {len(set(temp))}')