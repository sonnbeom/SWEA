n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# 가로 = 0 세로 1 대각 = 2
'''
00 01
10 11

'''

garo = [(0, 1), (1, 1)] #0 : 가로
sero = [(1,0), (1, 1)] #0 : 세로
cross = [(0, 1), (1, 0), (1, 1)]
ans = 0
def dfs(y, x, state):
    global ans
    if y == n-1 and x == n-1:
        ans += 1
        return
    if state == 0: # 가로

        for i in range(2):
            dy, dx = garo[i]
            nowY = y + dy
            nowX = x + dx
            if 0 <= nowY < n and 0 <= nowX < n and arr[nowY][nowX] != 1:
                if i == 0:
                    dfs(nowY, nowX, 0)
                elif i == 1:
                    if arr[y][x+1] != 1 and arr[y+1][x] != 1:
                        dfs(nowY, nowX, 2)

    elif state == 1:                 # 세로
         for i in range(2):
            dy, dx = sero[i]
            nowY = y + dy
            nowX = x + dx
            if 0 <= nowY < n and 0 <= nowX < n and arr[nowY][nowX] != 1:
                if i == 0:
                    dfs(nowY, nowX, 1)
                elif i == 1:
                    if arr[y][x+1] != 1 and arr[y+1][x] != 1:
                        dfs(nowY, nowX, 2)
                        
    elif state == 2:                 # 대각
         for i in range(3):
            dy, dx = cross[i]
            nowY = y + dy
            nowX = x + dx
            if 0 <= nowY < n and 0 <= nowX < n and arr[nowY][nowX] != 1:
                if i == 0:
                    dfs(nowY, nowX, 0)
                elif i == 1:
                    dfs(nowY, nowX, 1)
                elif i == 2:
                    if arr[y][x+1] != 1 and arr[y+1][x] != 1:
                        dfs(nowY, nowX, 2)
# y =0  x = 1시작
dfs(0, 1, 0)
print(ans)