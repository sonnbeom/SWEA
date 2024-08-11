'''
맨 아래 idx 99에서 2를 찾는다
while문을 돈다 idx > 0 조건으로

조건 1. 왼쪽 갈 수 있어?
왼쪽으로 갈 거면 계속 왼쪽
while문으로 간다 언제까지? 왼쪽에 숫자가 0일때까지

조건 2. 오른쪽으로 갈 거면 계속 오른쪽
while문으로 간다 언제까지? 오른쪽 숫자가 0일때까지

없으면 위로 한 칸
x값 반환
if y == 0 이면 x값 리턴  
00 01 02 

'''
arr = [list(map(int, input().split())) for _ in range(100)]
visited = [[False for _ in range(100)] for _ in range(100)]
y = 99
res = 0
x = 0
for i in range(100):
    if arr[99][i] == 2:
        x = i
        

while y >= 0:
    # 좌로 가는 거임
    if x > 0  and arr[y][x-1] == 1 and visited[y][x-1] == False:
        while x > 0 and arr[y][x-1] == 1:
            x -= 1
            visited[y][x] = True
    # 우로 이동
    elif x < 99 and arr[y][x+1] == 1 and visited[y][x+1] == False:
        while x < 99 and arr[y][x+1] == 1:
            x += 1
            visited[y][x] = True
    # 위로 이동
    else:
        y -= 1
        visited[y][x] = True
        
print(x)