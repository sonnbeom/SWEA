t, start  = map(int, input().split())

arr = [[0 for _ in range(101)] for _ in range(101)]
visited = [False for _ in range(101)]

tempList = list(map(int, input().split()))

for i in range(0, t, 2):
    a = tempList[i]
    b = tempList[i+1]
    arr[a][b] = 1 #인접 행렬로 만들기

depthList = []

def dfs(depth, start):
    visited[start] = True
    depthList.append((depth, start)) #dfs를 호출할 때마다 튜플의 형태로 depth와 노드를 튜플형태로 담는다.

    for i in range(1, 101): # 숫자 범위가 1~100이므로
        if arr[start][i] == 1 and visited[i] == False: # 방문하지 않았고, 
            dfs(depth+1, i)
            # visited[i] = False

dfs(1, start)
depthList.sort()

ans = 0
listLen = len(depthList)
depthMax = depthList[listLen-1][0]
print(depthMax)
for depth, node in depthList:
    if depth == depthMax:
        if node > ans:
            ans = node
print(ans)
