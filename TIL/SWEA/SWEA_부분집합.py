# visited = [False for _ in range(13)]
res = 0
n, k = map(int, (input().split()))
tempList = []

def dfs(depth, start, arr, visited):
    global res
    if depth > n:
        return
    if depth == n:
        if sum(arr) == k and set(arr) not in tempList:
            tempList.append(set(arr))
            res += 1
        return
    else:
        for i in range(start, 13):
            if visited[i] == False:
                arr.append(i)
                visited[i] = True
                dfs(depth+1, i, arr, visited)
                visited[i] = False

arr = []
visited = [False for _ in range(13)]
dfs(0, 1, arr, visited)
print(res)