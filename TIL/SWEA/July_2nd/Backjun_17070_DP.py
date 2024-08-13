def solution():
    dp[0][0][1] = 1
    for i in range(2, n):
        if arr[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]
    
    for y in range(1, n):
        for x in range(1, n):
            if arr[y][x] == 0 and arr[y-1][x] == 0 and arr[y][x-1] == 0:
                dp[2][y][x] = dp[2][y-1][x-1] + dp[1][y-1][x-1] + dp[0][y-1][x-1]
            if arr[y][x] == 0:
                dp[0][y][x] = dp[0][y][x-1] + dp[2][y][x-1]
                dp[1][y][x] = dp[1][y-1][x] + dp[2][y-1][x]
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# 가로 0 세로 1 대각 2
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
result = 0
solution()
for i in range(3):
    result += dp[i][n-1][n-1]

print(result)