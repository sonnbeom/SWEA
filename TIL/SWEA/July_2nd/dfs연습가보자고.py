m = 2
def dfs(req, start, depth, arr, result):
    if depth == 2:
        result.append(arr.copy())
        return
    for i in range(start, len(req)):
        arr.append(req[i])
        dfs(req, i+1, depth+1, arr, result)
        arr.pop()

req = [1,2,3]
result = []
dfs(req, 0, 0, [],result)
print(*result)