t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(y, x):
        queue = [(y,x)]
        depth = 1

        while queue:
            tempY, tempX = queue.pop(0)
            for i in range(4):
                nowX = dx[i] + tempX
                nowY = dy[i] + tempY
                if 0 <= nowX < n and 0 <= nowY < n and arr[nowY][nowX] == arr[tempY][tempX]+1:
                    depth += 1
                    queue.append((nowY, nowX))
        return depth
    maxDepth = 0
    tmpList = []
    for y in range(n):
        for x in range(n):
            depth = bfs(y, x)
            if depth >= maxDepth:
                maxDepth = depth
                tmpList.append((depth, arr[y][x]))

    tmpList.sort()
    res = tmpList[-1][1]

    for dep, node in tmpList:
        if dep == maxDepth:
            if node < res:
                res = node
    print(f'#{tc} {res} {maxDepth}')