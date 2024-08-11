n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(n)] for _ in range(n)]
def bfs(sy, sx):
    q = [(sy, sx)]
    ans = 0
    while q:
        y, x = q.pop(0)
        visited[y][x] = True
        for i in range(4):
            nowY = y + dy[i]
            nowX = x + dx[i]
            if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] != 1 and visited[nowY][nowX] == False:
                if arr[nowY][nowX] == 3:
                    ans = 1
                    break
                q.append((nowY, nowX))
    return ans
def findStart():
    for i in range(n):
        if 2 in arr[i]:
            return (i, arr[i].index(2))
    return (-1, -1)
start = findStart()
if start[0] == -1:
    print(0)
else:
    res = bfs(start[0], start[1])
    print(res)
