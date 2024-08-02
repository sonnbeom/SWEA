res = 0
n, k = map(int, (input().split()))
visited = [False for _ in range(13)]
resList = []
def dfs(start, depth, arr):
    global res
    if depth == n:
        if sum(arr) == k and set(arr) not in resList:
            res += 1
            resList.append(set(arr))
        return
    for i in range(start, 13):
        if visited[i] == False:
            arr.append(i)
            visited[i] = True
            dfs(i, depth+1, arr)
            visited[i] = False
            arr.pop()

for start in range(1, 13):            
    dfs(start, 0, [])
print(res)