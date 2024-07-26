'''
좌 우 하 상
방문하려는 곳이 이전까지의 비용 + 방문하려는 곳의 비용보다 저렴하다면 갱신
그렇지 않다면 냅둔다.

1. while문 돌린다 y, x = n일때까지
2. 그러면 도착하는 곳 하나라도 생기면 그만 둠
3. for문 완탐?

for문 완탐이면
접근하려는 곳의 우 상 하 돌려서 비교하고 갱신

'''

'''
우 상 하

00 01
10 11
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
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
                        dp[nowY][nowX] = min(dp[y][x] + arr[nowY][nowX], dp[nowY][nowX])
print(dp[n-1][n-1])

