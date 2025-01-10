import sys
sys.setrecursionlimit(1000000)
dy = [0, 0, 1, -1]
dx = [1,-1, 0, 0]

def range_check(y, x, n):
    if 0 <= y < n and 0 <= x < n:
        return True
    else:
        return False
def dfs(y, x, cnt, visited, n):
    global answer
    if y == n-1 and x == n-1:
        answer = min(answer, cnt)
        return
    if answer <= cnt:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not range_check(ny, nx, n):
            continue
        if visited[ny][nx]:
            continue
        if arr[ny][nx] == 0:
            visited[ny][nx] = True
            dfs(ny, nx, cnt+1, visited, n)
            visited[ny][nx] = False
        elif arr[ny][nx] == 1:
            visited[ny][nx] = True
            dfs(ny, nx, cnt, visited, n)
            visited[ny][nx] = False

n = int(input())
arr = []
for _ in range(n):
    li = list(map(int,input()))
    arr.append(li)
answer = 50*50+1
visited = [[False for _ in range(n)] for _ in range(n)]
dfs(0, 0, 0, visited, n)
print(answer)