t = int(input())
for testCase in range(1, t+1):
    res = 0
    n, k = map(int, (input().split()))
    tempList = []

    def dfs(depth, node, arr, visited):
        global res
        if depth > n:
            return
        if depth == n:
            if sum(arr) == k and set(arr) not in tempList:
                tempList.append(set(arr))
                res += 1
            return
        arr.append(node)
        visited[node] = True
        if depth < n:
            for i in range(1, 13):
                if visited[i] == False:
                    dfs(depth+1, i, arr, visited)

    arr = []
    visited = [False for _ in range(13)]
    dfs(0, 1, arr, visited)
    print(f'#{testCase} {res}')