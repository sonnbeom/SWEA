from collections import deque
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())
for testCase in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input())) for _ in range (n)]

    cost = [[999999 for _ in range(n)] for i in range(n)]     
    cost [0][0] = 0

    q = deque()
    q.append((0,0))

    while q:
        y,x = q.popleft()

        for direc in range(4):
            nowY = y + dy[direc]
            nowX = x + dx[direc]

            if 0 <= nowX < n and 0 <= nowY < n:
                if cost[nowY][nowX] > cost[y][x] + arr[nowY][nowX]:
                    cost[nowY][nowX] = cost[y][x] + arr[nowY][nowX]
                    q.append((nowY, nowX))

    print(f'#{testCase} {cost[n-1][n-1]}')
                    

