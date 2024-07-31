visited = [False for _ in range(13)]
res = 0
n, k = map(int, (input().split()))
tempList = []
def dfs(depth, n, node, arr, visited):
    global res
    if depth == n:
        if sum(arr) == k and arr not in tempList:
            tempList.append(arr)
            res += 1
        return
    
    arr.append(node)
    visited[node] = True
    if depth < n:
        for i in range(1, 13):
            if visited[i] == False:
                dfs(depth+1, n, i, arr, visited)

for i in range(1, 13):
    arr = []
    visited = [False for _ in range(13)]
    dfs(0, n, i, arr, visited)
    
print(res)