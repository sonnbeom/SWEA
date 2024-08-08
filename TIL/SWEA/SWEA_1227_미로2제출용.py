for k in range(10):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    visited = [[False for _ in range(100)] for _ in range(100)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    startY = 0
    startX = 0
    for i in range(100):
        if 2 in arr[i]:
            startX = arr[i].index(2)
            startY = i

    def bfs(y, x):
        q = [[y, x]]
        visited[y][x] = True
        while q:
            tempY, tempX = q.pop(0)
        
            for i in range(4):
                nowX = tempX + dx[i]
                nowY = tempY + dy[i]
                if 0 <= nowX < 100 and 0 <= nowY < 100:
                    if visited[nowY][nowX] == False and arr[nowY][nowX] == 0:
                        visited[nowY][nowX] = True
                        q.append([nowY, nowX])
                    elif arr[nowY][nowX] == 3:
                        return 1     
        return 0
    ans = bfs(startY, startX)
    print(f'#{t} {ans}')