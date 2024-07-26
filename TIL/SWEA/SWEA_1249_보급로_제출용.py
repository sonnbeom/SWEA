t = int(input())
for testCase in range(1, t+1):
    dx = [-1, 1, 0, 0]
    dy = [0 ,0, -1, 1]
    n = int(input())

    arr = [list(map(int, input())) for _ in range (n)]

    dp = [[-1 for _ in range(n)] for i in range(n)]     
    dp [0][0] = arr[0][0]

    for y in range(n):
        for x in range(n):
            for k in range(4):
                nowY = y + dy[k]
                nowX = x + dx[k]
                if 0 <= nowY < n and 0 <= nowX < n:
                    if dp[nowY][nowX] == -1:
                        dp[nowY][nowX] = dp[y][x] + arr[nowY][nowX]
                    else:
                        if dp[nowY][nowX] > dp[y][x] + arr[nowY][nowX]:
                            dp[nowY][nowX] = dp[y][x] + arr[nowY][nowX]
    print(f'#{testCase} {dp[n-1][n-1]}')

