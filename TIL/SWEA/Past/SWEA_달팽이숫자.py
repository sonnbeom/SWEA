'''
00 01
10 11 
우 하 좌 상

A. 조건문을 통과하면 숫자를 넣는다.

<조건문>
1. y x 0보다크거나 같고 n보단 작겠죠?
2. 가려고 하는 곳이 0이여야겠죠?

<숫자를 넣는다.>
1. 좌표 갱신해줘야겠죠

+++++++++ while문으로 바꾼 후 추가 요구 사항
2. count ++ 해줘야 하죠

B. 조건문을 통과하지 못하면 방향을 바꾼다

방향이 항상 저 패턴대로 움직여야 하므로
direc = (direc+1) % 4

''' 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
direc = 0
i = 2
y = 0
x = 0
arr[0][0] = 1
while i < n*n+1:
    nowX = x + dx[direc]
    nowY = y + dy[direc]
    if 0<= nowX < n and 0<= nowY < n and arr[nowY][nowX] == 0:
        arr[nowY][nowX] = i
        x = nowX
        y = nowY
        i += 1
    else:
        direc = (direc+1) % 4
for i in range(n):
    print(*arr[i])
    
'''
for i in range(2, n*n+1):
    nowX = x + dx[direc]
    nowY = y + dy[direc]
    if 0<= nowX < n and 0<= nowY < n and arr[nowY][nowX] == 0:
        arr[nowY][nowX] == i
        x = nowX
        y = nowY
    else:
        direc = (direc+1) % 3
'''    
