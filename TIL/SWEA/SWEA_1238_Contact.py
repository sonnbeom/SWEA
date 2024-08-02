t, start  = map(int, input().split())

arr = [[0 for _ in range(t)] for _ in range(t)]
visited = [[False for _ in range(t)] for _ in range(t)]

for i in range(t/2):
    a, b = map(int, input().split())
    arr[a][b] = b
    arr[b][a] = b

def dfs(y, x):
    pass
    
    
for i in range(t):
    for j in range(t):
        if arr[i][j] != 0 and visited[i][j] == False:
            dfs(i, j)
            pass
