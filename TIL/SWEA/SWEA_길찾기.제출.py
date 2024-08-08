for t in range(10):
    tc, n = map(int, input().split())

    tempInput = list(map(int, input().split()))
    maxNode = max(tempInput)

    arr = [[0 for _ in range(maxNode+1)] for _ in range(maxNode+1)]

    i = 0
    while tempInput:
        arr[tempInput[i]][tempInput[i+1]] = 1
        tempInput.pop(0)
        tempInput.pop(0)

    ans = 0

    def dfs(node, end):
        global ans
        if end == node:
            ans = 1
            return
        for i in range(maxNode+1):
            if arr[node][i] == 1:
                dfs(i, end)

    dfs(0, 99)
    print(f'#{tc} {ans}')