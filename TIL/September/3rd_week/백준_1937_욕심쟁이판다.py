import sys
sys.setrecursionlimit(10**9)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    if dp[y][x] != 0:
        return dp[y][x]

    else:
        dp[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if forest[ny][nx] > forest[y][x]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
        return dp[y][x]


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

maximum = 0

for y in range(n):
    for x in range(n):
        if dp[y][x] == 0:
            maximum = max(maximum, dfs(y, x))

print(maximum)
